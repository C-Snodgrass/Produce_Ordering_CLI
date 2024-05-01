import sqlite3


class Item:
    def __init__(self, name, variety, price_per_unit, quantity):
        self.name = name
        self.variety = variety
        self.price_per_unit = price_per_unit
        self.quantity = quantity

        # Connect to the SQLite database
        conn = sqlite3.connect('produce.db')
        cursor = conn.cursor()

        # Insert the item into the database
        cursor.execute("INSERT INTO items (name, variety, price_per_unit) VALUES (?, ?, ?)",
                       (self.name, self.variety, self.price_per_unit))
        conn.commit()

        # Close the database connection
        conn.close()

    def __str__(self):
        return f"{self.name} ({self.variety}) - ${self.price_per_unit:.2f}"
