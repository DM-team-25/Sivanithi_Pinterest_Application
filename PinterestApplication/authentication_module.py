from db_config import getConnection
import re
import msvcrt

class UserAuthentication:
    def __init__(self):
        self.username_pattern = r'^\w{4,15}$'
        self.email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        self.password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'

    def inputPassword(self, prompt="Enter password: "):
        print(prompt, end='', flush=True)
        password = ""
        while True:
            character = msvcrt.getch()
            if character == b'\r':
                print()
                break
            elif character == b'\x08':
                if len(password) > 0:
                    password = password[:-1]
                    print("\b \b", end='', flush=True)
            else:
                try:
                    char = character.decode()
                except UnicodeDecodeError:
                    continue
                password += char
                print("*", end='', flush=True)
        return password

    def validateUsername(self, username):
        return re.match(self.username_pattern, username) is not None

    def validateEmail(self, email):
        return re.match(self.email_pattern, email) is not None

    def validatePassword(self, password):
        return re.match(self.password_pattern, password) is not None

    def register(self):
        connection = getConnection()
        cursor = connection.cursor()

        while True:
            username = input("Enter username: ")
            if not self.validateUsername(username):
                print("Invalid username! Username must be 4-15 characters long and contain only letters, numbers, or underscore.")
                continue

            cursor.execute("SELECT id FROM users WHERE username=%s", (username,))
            if cursor.fetchone():
                print("Username already exists. Try another.")
                continue
            break

        while True:
            email = input("Enter email: ")
            if not self.validateEmail(email):
                print("Invalid email! Email must contain '@' and '.'") 
                continue

            cursor.execute("SELECT id FROM users WHERE email=%s", (email,))
            if cursor.fetchone():
                print("Email already registered. Try another.")
                continue
            break

        while True:
            password = self.inputPassword("Enter password: ")
            if not self.validatePassword(password):
                print("Weak password! Password must be at least 8 characters long, include uppercase and lowercase letters, a number, and a special character.")
                continue
            confirm_password = self.inputPassword("Confirm password: ")
            if password != confirm_password:
                print("Passwords do not match. Try again.")
                continue
            break

        while True:
            role = input("Enter role (seller/buyer): ").lower()
            if role not in ['seller', 'buyer']:
                print("Role must be 'seller' or 'buyer'. Try again.")
            else:
                break

        try:
            cursor.execute(
                "INSERT INTO users (username, email, password, role) VALUES (%s, %s, %s, %s)",   # Runs an SQL query to save the user info in the users table.
                (username, email, password, role)
            )
            connection.commit()
            print("Registration successful!")
        except Exception as exception:
            print("Error:", exception)
        finally:
            connection.close()

    def login(self):
        connection = getConnection()   # Connects to database and creates cursor.
        cursor = connection.cursor()

        username = input("Enter username: ")
        password = self.inputPassword("Enter password: ")

        cursor.execute("SELECT id, username, password, role FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()

        connection.close()

        if user and password == user[2]:
            print(f"Welcome {user[1]} ({user[3]})!")
            return {"id": user[0], "username": user[1], "role": user[3]}
        else:
            print("Invalid credentials!")
            return None
