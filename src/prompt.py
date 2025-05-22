import json

def load_menu():
    # Construct the absolute path to menu.json relative to this file (prompt.py)
    # This makes it robust to where the script is called from.
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    menu_file_path = os.path.join(dir_path, 'menu.json')

    try:
        with open(menu_file_path, "r") as f:
            menu_data = json.load(f)
    except FileNotFoundError:
        # Fallback or error handling if menu.json is not found
        # For now, returning an error message within the menu string
        return "Error: menu.json not found. Please contact support."
    except json.JSONDecodeError:
        return "Error: menu.json is not valid JSON. Please contact support."

    menu_string = "# Zomato Menu\n\n"
    for category, items in menu_data.items():
        menu_string += f"## {category}\n\n"
        for item, price in items.items():
            menu_string += f"- {item} - ${price:.2f}\n"
        menu_string += "\n"
    return menu_string

def get_system_instruction(menu_string_from_json):
    # This function now correctly uses the passed menu_string_from_json
    return f"""
You are Food OrderBot, \
an automated service to collect orders for an online restaurant. \
You first greet the customer, then collects the order, \
and then asks if it's a pickup or delivery. \
You wait to collect the entire order, then summarize it and check for a final \
time if the customer wants to add anything else. \
If it's a delivery, you ask for an address. \
IMPORTANT: Think and check your calculation before asking for the final payment!
Finally you collect the payment.\
Make sure to clarify all options, extras and sizes to uniquely \
identify the item from the menu.\
You respond in a short, very conversational friendly style. \
The menu includes:- \n\n{menu_string_from_json}
"""

# Initialize system_instruction with the dynamically loaded and formatted menu
system_instruction = get_system_instruction(load_menu())
