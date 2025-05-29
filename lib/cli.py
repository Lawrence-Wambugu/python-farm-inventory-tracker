from helpers import add_item, view_inventory, update_item, delete_item, get_categories

def main():
    while True:
        print("\nFarm Inventory Tracker")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            name = input("Enter item name (e.g., Maize, Cow, Tractor): ")
            try:
                quantity = float(input("Enter quantity: "))
                if quantity < 0:
                    print("Quantity cannot be negative.")
                    continue
            except ValueError:
                print("Invalid quantity. Please enter a number.")
                continue
            # Display available categories
            categories = get_categories()
            print("Available categories:")
            for cat_id, cat_name in categories:
                print(f"{cat_id}. {cat_name}")
            category_name = input("Enter category name (or new category): ")
            add_item(name, quantity, category_name)

        elif choice == "2":
            view_inventory()

        elif choice == "3":
            view_inventory()
            try:
                item_id = int(input("Enter item ID to update: "))
                name = input("Enter new name (press Enter to skip): ")
                quantity_input = input("Enter new quantity (press Enter to skip): ")
                quantity = float(quantity_input) if quantity_input else None
                if quantity is not None and quantity < 0:
                    print("Quantity cannot be negative.")
                    continue
                category_name = input("Enter new category name (press Enter to skip): ")
                update_item(item_id, name or None, quantity, category_name or None)
            except ValueError:
                print("Invalid input. Please enter a valid item ID or quantity.")
                continue

        elif choice == "4":
            view_inventory()
            try:
                item_id = int(input("Enter item ID to delete: "))
                delete_item(item_id)
            except ValueError:
                print("Invalid input. Please enter a valid item ID.")
                continue

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()