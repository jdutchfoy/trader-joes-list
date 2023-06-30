import unittest
from shopping.list import create_list, add_item, remove_item

class TestGroceryList(unittest.TestCase):
    def test_create_list(self):
        # Test the creation of an empty shopping list
        shopping_list = create_list()
        self.assertEqual(shopping_list, [])

    def test_add_item(self):
        # Test adding an item to the shopping list
        shopping_list = create_list()
        add_item(shopping_list, "Apples")
        self.assertEqual(shopping_list, ["Apples"])

    def test_remove_item(self):
        # Test removing an item from the shopping list
        shopping_list = create_list()
        add_item(shopping_list, "Apples")
        remove_item(shopping_list, "Apples")
        self.assertEqual(shopping_list, [])

if __name__ == "__main__":
    # Run the tests
    unittest.main()
