user_credentials = {}

#function to register user
def register_user():
    username = input("Enter your username: ")

    #check to see if username already existis
    if username in user_credentials:
            print("Username already exists. Please choose a different username!")
    else:
        password = input("Enter a password: ")
        user_credentials[username] = password
        print("Registration successful")

#function to login user
def login_user():
    print("login:")
    username = input("Enter your username: ")
    password = input("Enter your password: ")   

    #check to see if username and password match
    if username in user_credentials and user_credentials[username] == password:
        print("Welcome back!")
    else:
        print("Invalid username or password. Please try again.")


#main meny
def authentication_system():
    while True:
        print("Basic Authentication System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            register_user()
        elif option == "2":
            login_user()
        elif option == "3":
            print("Exiting the System")
            return False
            #Break
        else:
            print("Invalid choice. Please choose from options 1,2 or 3")

authentication_system()

    