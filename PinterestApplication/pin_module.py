from db_config import getConnection


class Pin:
    def uploadPin(self, seller_id):
        connection = getConnection()
        cursor = connection.cursor()

        product_name = input("Enter product name: ")
        description = input("Enter description: ")
        image_path = input("Enter image path: ")
        price = float(input("Enter price: "))

        try:
            cursor.execute(
                """
                INSERT INTO pins (seller_id, product_name, description, price, image_path)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (seller_id, product_name, description, price, image_path)
            )
            connection.commit()
            print("Pin uploaded successfully!")
        except Exception as exception:
            print("Error:", exception)
        finally:
            connection.close()

    def viewAllPins(self):
        connection = getConnection()
        cursor = connection.cursor()

        cursor.execute("SELECT id, product_name, description, price FROM pins")
        pins = cursor.fetchall()

        if pins:
            print("\n--- Available Pins ---")
            for pin in pins:
                print(f"ID: {pin[0]} | {pin[1]} - {pin[2]} | Price: ₹{pin[3]}")
        else:
            print("No pins available.")

        connection.close()

    def deletePin(self, seller_id):
        connection = getConnection()
        cursor = connection.cursor()

        pin_id = input("Enter Pin ID to delete: ")

        try:
            cursor.execute("DELETE FROM pins WHERE id=%s AND seller_id=%s", (pin_id, seller_id))
            connection.commit()
            if cursor.rowcount > 0:
                print("Pin deleted successfully!")
            else:
                print("Pin not found or unauthorized!")
        except Exception as exception:
            print("Error:", exception)
        finally:
            connection.close()
