import unittest
import json
import os
from unittest.mock import patch

# Add src to sys.path to allow direct import of src modules
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestMenuSystem(unittest.TestCase):

    def setUp(self): 
        """
        This method is called before each test.
        Start patching here, then import modules.
        The target of the patch should be where the object is looked up,
        which is 'openai.OpenAI' as imported in src.llm.
        """
        self.openai_patcher = patch('openai.OpenAI') # Changed patch target
        self.mock_openai_client_constructor = self.openai_patcher.start()
        # self.mock_openai_client_constructor will be a mock of the OpenAI class itself.
        # Instances can be checked via its return_value: self.mock_openai_client_constructor.return_value

        # Now it's safe to import modules that might trigger OpenAI client initialization indirectly
        from app import format_menu_for_display
        self.format_menu_for_display = format_menu_for_display
        
        from src.prompt import load_menu, get_system_instruction
        self.load_menu = load_menu
        self.get_system_instruction = get_system_instruction

        self.SAMPLE_MENU_DATA = {
          "Pizzas": {
            "Margherita Test": 10.00,
            "Pepperoni Test": 12.00
          },
          "Beverages": {
            "Test Cola": 2.00
          }
        }
        self.ACTUAL_MENU_FILE_PATH = "src/menu.json"

    def tearDown(self):
        """
        This method is called after each test.
        Stop the patcher.
        """
        self.openai_patcher.stop()

    def test_load_actual_menu_json(self): 
        """Tests loading the actual src/menu.json file."""
        try:
            menu_data_string = self.load_menu() 
        except FileNotFoundError:
            self.fail(f"Menu file not found at {self.ACTUAL_MENU_FILE_PATH}. Ensure the file exists and path is correct.")
        except json.JSONDecodeError:
            self.fail(f"Menu file at {self.ACTUAL_MENU_FILE_PATH} is not a valid JSON.")

        self.assertIsNotNone(menu_data_string, "Loaded menu data string should not be None.")
        self.assertIsInstance(menu_data_string, str, "load_menu should return a string.")
        self.assertIn("Pizzas", menu_data_string)
        self.assertIn("Margherita", menu_data_string) 
        self.assertIn("$10.99", menu_data_string)

    def test_get_system_instruction_with_menu(self):
        """Tests if the system prompt is correctly generated with menu data."""
        menu_string = self.load_menu()
        system_instruction = self.get_system_instruction(menu_string)

        self.assertIsInstance(system_instruction, str)
        self.assertIn("You are Food OrderBot", system_instruction)
        self.assertIn("The menu includes:-", system_instruction)
        self.assertIn("Margherita", system_instruction)
        self.assertIn("$10.99", system_instruction) 
        self.assertIn("Sushi Platter", system_instruction)
        self.assertIn("$25.00", system_instruction)

    def test_format_menu_for_display_from_app(self):
        """Tests the format_menu_for_display function from app.py using sample data."""
        formatted_string = self.format_menu_for_display(self.SAMPLE_MENU_DATA)
        
        self.assertIsInstance(formatted_string, str)
        self.assertIn("**Pizzas**", formatted_string)
        self.assertIn("- Margherita Test: $10.00", formatted_string)
        self.assertIn("**Beverages**", formatted_string)
        self.assertIn("- Test Cola: $2.00", formatted_string)
        self.assertTrue(formatted_string.startswith("Welcome! Here is our menu:\n\n"))

    def test_load_menu_function_returns_string(self):
        """Tests that src.prompt.load_menu() returns a string."""
        menu_output = self.load_menu()
        self.assertIsInstance(menu_output, str)
        self.assertGreater(len(menu_output), 50) 
        self.assertIn("# Zomato Menu", menu_output)

if __name__ == '__main__':
    unittest.main()
