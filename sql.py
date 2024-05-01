import os
import sqlite3


def insert_synthetic_produce():
    conn = sqlite3.connect("produce.db")
    cursor = conn.cursor()
    synthetic_data = [
        ("apple", "lady in the snow", 50, 2.99),
        ("carrot", "dutch", 30, 1.49),
        ("apple", "jazz", 70, 1.79),
        ("tomato", "ox heart", 40, 2.29),
        ("apricot", "moorpark", 60, 2.49)
    ]
    # SQL statement to insert data into the produce table
    sql_insert = "INSERT INTO produce (type, variety, available, price) VALUES (?, ?, ?, ?)"
    
    # Bulk insert data into the produce table
    cursor.executemany(sql_insert, synthetic_data)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()


# command to ceate an admin table in sqlite db
create_admin_table = """CREATE TABLE IF NOT EXISTS admin(
    admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name NOT NULL,
    password NOT NULL
);"""

# Create a variable for the next SQL statement
create_produce_table = """CREATE TABLE IF NOT EXISTS produce (
    produce_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    variety TEXT,
    available INTEGER,
    price DOUBLE
);"""

# Create a table to represent an order
create_order_table = """CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    produce_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (produce_id) REFERENCES produce(produce_id)
);"""


def add_an_admin(username, password, cursor, connection):
    username = username.lower()
    cursor.execute("INSERT OR IGNORE INTO admin (user, password) VALUES (?, ?);", (username, password))
    connection.commit()


def add_produce(veg_type, variety, available, price, cursor, connection):
    veg_type = veg_type.lower()
    variety = variety.lower()
    cursor.execute("INSERT OR IGNORE INTO produce (type, variety, available, price) VALUES (?, ?, ?, ?);",
                   (veg_type, variety, available, price))
    connection.commit()


def create_tables_if_not_exist():
    # Check if tables exist
    connection = sqlite3.connect('produce.db')
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('admin', 'produce', 'orders')")
    existing_tables = cursor.fetchall()
    existing_table_names = [table[0] for table in existing_tables]

    # Create tables that don't exist
    if 'admin' not in existing_table_names:
        cursor.execute(create_admin_table)
    if 'produce' not in existing_table_names:
        cursor.execute(create_produce_table)
    if 'orders' not in existing_table_names:
        cursor.execute(create_order_table)

    # Commit changes and close connection
    connection.commit()
    connection.close()


# TODO pass the cursor
def create_new_order(items):
    # Connect to the SQLite database
    conn = sqlite3.connect('produce.db')
    cursor = conn.cursor()
    quantity = input("Enter the quantity: ")
    # Insert the new orders into the orders table
    cursor.executemany("INSERT INTO orders (produce_id, quantity) VALUES (?, ?)", items)
    conn.commit()

    print("Orders created successfully.")

    # Close the database connection
    conn.close()
    # Close the database connection
    conn.close()
    return


# TODO pass the cursor? probably pass the whole order to here and bulk add.. shown in the tut
def add_to_order():
    return


# TODO eddit produce entry
def edit_produce_entry():
    return


# check if my db file exists
def db_exists(db_file):
    return os.path.exists(db_file)
