from openai import OpenAI
from src.prompt import get_system_instruction, load_menu # Updated import

client = OpenAI()

# Load menu and generate system instruction
# This ensures that menu loading and prompt generation happen when llm.py is loaded.
try:
    menu_string = load_menu()
    SYSTEM_INSTRUCTION = get_system_instruction(menu_string)
except FileNotFoundError:
    SYSTEM_INSTRUCTION = "Error: The menu file could not be loaded. Please contact support."
except Exception as e:
    SYSTEM_INSTRUCTION = f"An unexpected error occurred while loading the menu for the prompt: {e}"

# This 'messages' list in llm.py is a bit confusing if app.py also maintains one.
# For clarity, the main conversation history should be managed in app.py.
# This 'messages' here will just serve as the initial system message template.
# We will not append to it here.
INITIAL_MESSAGES_TEMPLATE = [
    {"role":"system","content":SYSTEM_INSTRUCTION}
]

def ask_order(current_conversation_messages, model="gpt-3.5-turbo", temperature = 0):
    """
    Sends the current conversation to OpenAI API.
    Prepends the system instruction to the current conversation.
    'current_conversation_messages' should be a list of user and assistant messages.
    """
    
    # Prepend the system instruction to the current conversation history
    messages_to_send = INITIAL_MESSAGES_TEMPLATE + current_conversation_messages

    response = client.chat.completions.create(
        model = model,
        messages = messages_to_send,
        temperature = temperature
    )

    return response.choices[0].message.content
