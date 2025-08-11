from db_config import getConnection
from datetime import datetime


class Order:
    def placeOrder(self, buyer_id):
        connection = getConnection()
        cursor = connection.cursor()

        cursor.execute("SELECT id, product_name, price FROM pins")
        pins = cursor.fetchall()

        if not pins:
            print("No pins available for ordering.")
            connection.close()
            return

        print("\n--- Available Pins ---")
        for pin in pins:
            print(f"ID: {pin[0]} | {pin[1]} | Price: ₹{pin[2]}")

        try:
            pin_id = int(input("Enter Pin ID to order: "))
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Please enter valid numbers for Pin ID and quantity.")
            connection.close()
            return

        cursor.execute("SELECT price FROM pins WHERE id=%s", (pin_id,))
        price_data = cursor.fetchone()

        if not price_data:
            print("Invalid Pin ID.")
            connection.close()
            return

        price = float(price_data[0])
        total_price = price * quantity

        try:
            cursor.execute(
                "INSERT INTO orders (buyer_id, pin_id, quantity, total_price) VALUES (%s, %s, %s, %s)",
                (buyer_id, pin_id, quantity, total_price)
            )
            connection.commit()
            print(f"Order placed successfully! Total: ₹{total_price}")
        except Exception as exception:
            print("Error:", exception)
        finally:
            connection.close()

    def viewOrders(self, buyer_id):
        connection = getConnection()
        cursor = connection.cursor()

        cursor.execute(
            """SELECT o.id, p.product_name, o.quantity, o.total_price, o.order_date
               FROM orders o
               JOIN pins p ON o.pin_id = p.id
               WHERE o.buyer_id = %s""", (buyer_id,)
        )
        orders = cursor.fetchall()

        if orders:
            print("\n--- My Orders ---")
            for order in orders:
                print(f"Order ID: {order[0]} | Product: {order[1]} | Qty: {order[2]} | Total: ₹{order[3]} | Date: {order[4]}")
        else:
            print("No orders found.")

        connection.close()
