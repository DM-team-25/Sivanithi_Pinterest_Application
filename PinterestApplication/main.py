from authentication_module import UserAuthentication
from pin_module import Pin
from order_module import Order


class MainMenu:
    def __init__(self, user_info):
        self.user_info = user_info
        self.pin = Pin()
        self.order = Order()

    def showMenu(self):
        if self.user_info["role"] == "seller":
            while True:
                print("\n--- Seller Menu ---")
                print("1. Upload Pin")
                print("2. View All Pins")
                print("3. Delete Pin")
                print("4. Logout")
                choice = input("Enter choice: ")

                if choice == "1":
                    self.pin.uploadPin(self.user_info["id"])
                elif choice == "2":
                    self.pin.viewAllPins()
                elif choice == "3":
                    self.pin.deletePin(self.user_info["id"])
                elif choice == "4":
                    break
                else:
                    print("Invalid choice!")

        elif self.user_info["role"] == "buyer":
            while True:
                print("\n--- Buyer Menu ---")
                print("1. View All Pins")
                print("2. Place Order")
                print("3. View My Orders")
                print("4. Logout")
                choice = input("Enter choice: ")

                if choice == "1":
                    self.pin.viewAllPins()
                elif choice == "2":
                    self.order.placeOrder(self.user_info["id"])
                elif choice == "3":
                    self.order.viewOrders(self.user_info["id"])
                elif choice == "4":
                    break
                else:
                    print("Invalid choice!")

def main():
    user_obj = UserAuthentication()

    while True:
        print("\n--- Pinterest Application ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            user_obj.register()
        elif choice == "2":
            user_info = user_obj.login()
            if user_info:
                menu = MainMenu(user_info)
                menu.showMenu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
