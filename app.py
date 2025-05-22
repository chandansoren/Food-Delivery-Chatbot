import chainlit as cl
from src.llm import ask_order # Removed 'messages' import from src.llm
import json

# This will store the conversation history for the current chat session
# Chainlit's @cl.on_chat_start and @cl.on_message will manage the state per session.
# We don't need a global 'messages' list here anymore for the conversation.

def format_menu_for_display(menu_data):
    menu_string = "Welcome! Here is our menu:\n\n"
    for category, items in menu_data.items():
        menu_string += f"**{category}**\n"
        for item, price in items.items():
            menu_string += f"- {item}: ${price:.2f}\n"
        menu_string += "\n"
    return menu_string

@cl.on_chat_start
async def start_chat():
    # Initialize an empty conversation history for the session
    cl.user_session.set("conversation_history", []) 
    
    try:
        with open("src/menu.json", "r") as f:
            menu_data = json.load(f)
        
        formatted_menu = format_menu_for_display(menu_data)
        
        await cl.Message(
            content=formatted_menu,
            author="OrderBot"
        ).send()
    except FileNotFoundError:
        await cl.Message(
            content="Error: The menu file (src/menu.json) was not found. Please ensure it exists in the 'src' directory.",
            author="OrderBot"
        ).send()
    except json.JSONDecodeError:
        await cl.Message(
            content="Error: The menu file (src/menu.json) is not a valid JSON file. Please check its format.",
            author="OrderBot"
        ).send()
    except Exception as e:
        await cl.Message(
            content=f"An unexpected error occurred while loading the menu: {e}. Please contact support.",
            author="OrderBot"
        ).send()

@cl.on_message
async def main(message: cl.Message):
    # Retrieve the conversation history from the user session
    conversation_history = cl.user_session.get("conversation_history")

    # Add the user's message to the history
    conversation_history.append({"role": "user", "content": message.content})
    
    # Get the response from the LLM
    # ask_order now expects only the current conversation (without system message)
    response_content = ask_order(conversation_history)
    
    # Add the assistant's response to the history
    conversation_history.append({"role": "assistant", "content": response_content})
    
    # Update the conversation history in the user session
    cl.user_session.set("conversation_history", conversation_history)

    # Send a response back to the user
    await cl.Message(
        content=response_content,
    ).send()
