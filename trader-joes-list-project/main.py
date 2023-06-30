# Import the necessary functions from the shopping.list module
from shopping.list import create_list, add_item, remove_item, view_list

def main():
    # Create an empty shopping list
    shopping_list = create_list()
    
    while True:
        print("\nWelcome to Trader Joe's Grocery List!")
        print("1. Add item to the list")
        print("2. Remove item from the list")
        print("3. View the list")
        print("4. Exit")
        
        # Ask the user for their choice
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            # Add an item to the shopping list
            item = input("Enter the item to add: ")
            add_item(shopping_list, item)
        elif choice == '2':
            # Remove an item from the shopping list
            item = input("Enter the item to remove: ")
            remove_item(shopping_list, item)
        elif choice == '3':
            # View the current list
            view_list(shopping_list)
        elif choice == '4':
            # Exit the program
            print("Exiting the program...")
            break
        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Call the main function to start the program
    main()
