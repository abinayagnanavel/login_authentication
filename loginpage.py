import os

USERS_FILE = 'users.txt'

# Ensure file exists
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, 'w') as f:
        pass  # create empty file

def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    with open(USERS_FILE, 'r') as f:
        for line in f:
            stored_user, _ = line.strip().split(':')
            if stored_user == username:
                print("Username already exists!")
                return

    with open(USERS_FILE, 'a') as f:
        f.write(f"{username}:{password}\n")
    print("✅ Registration successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(USERS_FILE, 'r') as f:
        for line in f:
            stored_user, stored_pass = line.strip().split(':')
            if stored_user == username and stored_pass == password:
                print("✅ Login successful!")
                secured_page(username)
                return
    print("❌ Invalid username or password.")

def secured_page(username):
    print(f"\n🚀 Welcome to the secured page, {username}!")
    print("Only logged-in users can see this.\n")

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter choice (1/2/3): ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()
