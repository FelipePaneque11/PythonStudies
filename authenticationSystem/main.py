import re #import for regular expressions
import hashlib #import for hashing
from datetime import datetime #import for date and time
import os

#hash password function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#Password checker function
def check_strong_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    if not re.search(r'[A-Z]', password):
        return False, "Password must have at least one uppercase letter."

    if not re.search(r'[0-9]', password):
        return False, "Password must have at least one number."

    if not re.search(r'[!@#$%^&*():{}|.<>?~]', password):
        return False, "Password must have at least one special character."

    return True, "Password is strong."
    
#function to log user activities
def log_events(event):
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    #add file on the same folder
    folder = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(folder, "audit_log.txt")

    with open(log_path, "a") as log_file:
        log_file.write(f"[{timestamp}] {event}\n")


#Registration function
def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    is_valid, feedback = check_strong_password(password)
    
    if not is_valid:
        print("Password is not strong enough")
        print(feedback)
        log_events(f"Registration failed for user {username}.")
        return

    #Hash password
    hashed_password = hash_password(password)

   #add file on the same folder
    folder = os.path.dirname(os.path.abspath(__file__))
    user_path = os.path.join(folder, "users.txt")
   
    with open(user_path, "a") as file:
        file.write(f"{username}:{hashed_password}\n")
    
    print("User Registration was Successful!")
    log_events(f"{username} successfully Registered.")

#Login function
def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    #add file on the same folder
    folder = os.path.dirname(os.path.abspath(__file__))
    user_path = os.path.join(folder, "users.txt")

    with open(user_path, "r") as file:
        users = file.readlines()

    for user in users:
        stored_username, stored_password = user.strip().split(":")
        if(username == stored_username and hash_password(password) == stored_password):
            print("login successful")
            log_events(f"{username} successfully logged in.")
            post_login_menu(username)
            return
        
    print("Invalid username or password")
    log_events(f"Failed login attempt for user {username}")

#Function to display Post login menu
def post_login_menu(username):
    while True:
        print("\nPost-Login Menu")
        print("1. View my logs")
        print("2. Logout")

        choice = input("what would you like to do? ")

        if choice == "1":
            view_logs(username)
        elif choice == "2":
            log_events(f"User '{username}' logged out")
            print("Logged out successfully")
            break
        else:
            print("Invalid choice. Please try again")

#Function to view logs
def view_logs(username):
    print(f"\nLogs for user '{username}'")

    #add file on the same folder
    folder = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(folder, "audit_log.txt")

    with open(log_path, "r") as log_file:
        logs = log_file.readlines()
        
    user_logs = [log.strip() for log in logs if username in log]
    if user_logs:
        for log in user_logs:
            print(log)
    else:
        print("No logs were found in your account.")



def main():
    while True:
        print("Welcome to the User Registration System")
        print("1. Register ")
        print("2. Login")
        print("3. Exit")

        choice = input("What would you like to do ?")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Exiting the system....")
            break
        else:
            print("Invalid choice. Please try again.")

main()