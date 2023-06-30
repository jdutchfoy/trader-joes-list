def create_list():
    # Create an empty shopping list
    return []

def add_item(shopping_list, item):
    # Add to the shopping list
    shopping_list.append(item)
    print(f"Added '{item}' to the list.")

def remove_item(shopping_list, item):
    # Check if the item exists in the shopping list and remove it
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed '{item}' from the list.")
    else:
        # Handle the case when the item is not found in the list
        print(f"'{item}' not found in the list.")

def view_list(shopping_list):
    # contents of the shopping list
    if shopping_list:
        print("\nCurrent Grocery List:")
        for item in shopping_list:
            print(item)
    else:
        # Handle the case when the shopping list is empty
        print("\nThe list is empty.")
