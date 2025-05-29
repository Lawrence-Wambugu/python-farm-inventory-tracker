# Farm Inventory Tracker

The Farm Inventory Tracker is a Python command-line interface (CLI) application designed to help farmers manage their inventory of crops, livestock, and equipment. Built with Python, SQLAlchemy, and a SQLite database, it allows users to add, view, update, and delete inventory items, filter items by category, and generate summary reports. The application uses a modular structure, with database operations separated from user interaction, and leverages Python data structures like lists and dictionaries for efficient data handling. This project solves the real-world problem of tracking farm resources, ensuring farmers can monitor stock levels and changes effectively.

## Setup

To set up and run the Farm Inventory Tracker, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Lawrence-Wambugu/farm-inventory-tracker.git
   ```
   

2. **Navigate to the Project Directory**:
   ```bash
   cd farm-inventory-tracker
   ```

3. **Install Dependencies**:
   Ensure you have Pipenv installed, then install the required packages:
   ```bash
   pipenv install
   ```

4. **Activate the Virtual Environment**:
   ```bash
   pipenv shell
   ```

5. **Set Up the Database**:
   - Initialize the database schema:
     ```bash
     cd lib/db
     alembic upgrade head
     ```
   - Seed the database with sample data:
     ```bash
     cd ../..
     python lib/db/seed.py
     ```

6. **Run the CLI**:
   ```bash
   python lib/cli.py
   ```

## Usage

The CLI provides a menu-driven interface with the following options:
1. **Add Item**: Add a new item (e.g., Maize, 500, Crops) to the inventory.
2. **View Inventory**: Display all items with their IDs, names, quantities, and categories.
3. **Update Item**: Modify an item’s name, quantity, or category by ID.
4. **Delete Item**: Remove an item by ID, logging the deletion as a transaction.
5. **Filter by Category**: View items in a specific category (e.g., Crops).
6. **Generate Summary Report**: Show total quantities per category (e.g., Crops: 800 units).
7. **Exit**: Close the application.

Example interaction:
```
Farm Inventory Tracker
1. Add Item
2. View Inventory
3. Update Item
4. Delete Item
5. Filter by Category
6. Generate Summary Report
7. Exit
Enter choice (1-7): 2
Farm Inventory:
ID | Name | Quantity | Category
----------------------------------------
1 | Maize | 500.0 | Crops
2 | Wheat | 300.0 | Crops
3 | Cows | 20.0 | Livestock
...
```

## Project Structure

- **`lib/cli.py`**:
  The main CLI script that provides a menu-driven interface for user interaction. It uses `input()` to capture user choices and calls functions from `helpers.py` to perform database operations. The script handles user input validation and displays results in a clear, tabular format.

- **`lib/helpers.py`**:
  Contains functions for database operations, keeping the CLI logic separate for modularity. Functions include:
  - `get_session()`: Creates a SQLAlchemy session for database access.
  - `add_item(name, quantity, category_name)`: Adds a new item and logs a transaction.
  - `view_inventory()`: Displays all items with their categories.
  - `update_item(item_id, name, quantity, category_name)`: Updates an item’s details and logs quantity changes.
  - `delete_item(item_id)`: Deletes an item and its transactions.
  - `get_categories()`: Returns a list of category IDs and names.
  - `filter_by_category(category_name)`: Displays items in a specific category.
  - `generate_summary_report()`: Shows total quantities per category using a dictionary.

- **`lib/db/models.py`**:
  Defines SQLAlchemy models for the database:
  - `Category`: Stores category names (e.g., Crops, Livestock, Equipment) with a one-to-many relationship to Items.
  - `Item`: Stores item details (name, quantity, category_id) with relationships to Category and Transactions.
  - `Transaction`: Logs item changes (add, update, delete) with item_id, quantity, type, and timestamp.

- **`lib/db/seed.py`**:
  Populates the database with sample data (e.g., Categories: Crops, Livestock, Equipment; Items: Maize, Cows, Tractor) for testing.

- **`lib/debug.py`**:
  A utility script to verify database setup by printing all categories, items, and transactions.

- **`lib/db/migrations/`**:
  Contains Alembic migration scripts to manage database schema changes.

- **`Pipfile` and `Pipfile.lock`**:
  Define the virtual environment and dependencies (SQLAlchemy, Alembic, Click) using Pipenv.

## Database Schema

The application uses a SQLite database (`farm_inventory.db`) with three related tables:
- **Categories**: Stores unique category names with an ID as the primary key.
- **Items**: Stores inventory items with name, quantity, and a foreign key to Categories.
- **Transactions**: Logs item changes (add, update, delete) with a foreign key to Items, including quantity and timestamp.

Relationships:
- One-to-many: `Category` to `Item` (one category has many items).
- One-to-many: `Item` to `Transaction` (one item has many transactions).

## Requirements Met

- **CLI Application**: A menu-driven CLI for managing farm inventory, solving the real-world problem of resource tracking.
- **SQLAlchemy ORM**: Uses SQLAlchemy with three related tables (Categories, Items, Transactions).
- **Modular Structure**: Separates CLI logic (`cli.py`), database operations (`helpers.py`), and models (`models.py`).
- **Data Structures**: Uses lists (e.g., category lists) and dictionaries (e.g., summary report).
- **Virtual Environment**: Managed with Pipenv, including SQLAlchemy and Alembic.

## Future Improvements

- Add case-insensitive category filtering.
- Include a transaction history view to track all changes.
- Enhance the summary report with additional metrics (e.g., average quantity per item).

## Resources

- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)