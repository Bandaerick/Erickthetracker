import hashlib
import getpass

password_manager = {}

def create_account():
    print("Creating account...")
    username = input("Enter your desired username: ")
    print("Username entered:", username)
    password = getpass.getpass("Enter your desired password: ")
    print("Password entered (hidden for security)")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account created successfully!")

def login():
    print("Logging in...")
    username = input("Enter your username: ")
    print("Username entered:", username)
    password = getpass.getpass("Enter your password: ")
    print("Password entered (hidden for security)")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password")

def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
