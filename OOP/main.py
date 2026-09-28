#Book Class
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.authpr = author
        self.genre = genre
        self.is_available = True


    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.title} has been borrowed")
        else:
            print(f"Sorry, {self.title} is not currently available to borrow.")

    def return_book(self):
        self.is_available = True
        print(f"{self.title} has been returned")

    def isAvailable(self):
        if self.is_available:
            print(f"The book {self.title} is available to borrow")
        else:
             print(f"The book {self.title} is not available to borrow")

       

book1 = Book("Harry Potter and the Philosopher's Stone", "J.K Rowling", "Fantasy")
book2 = Book("Harry Potter and the Chamber of Secrets", "J.K Rowling", "Fantasy")

book1.borrow() #Harry Potter and the Philosopher's Stone has been borrowed
book1.isAvailable() #The book Harry Potter and the Philosopher's Stone is not available to borrow
book1.return_book() #Harry Potter and the Philosopher's Stone has been returned
book1.isAvailable() #The book Harry Potter and the Philosopher's Stone is available to borrow

#User Class
class User:
    def __init__(self, username, password):
        self.username = username
#encapsulation
        self.__password = password # __ = private


    def authenticate(self, password):
        return self.__password == password

    def login(self):
        print(f"{self.username} has logged in")

#Inheritance
class Admin(User):
    def access_logs(self):
        print(f"{self.username} is accessing the logs")

    def login(self):
        print("admin has logged in")


user = User("user", "mypassword")
admin = Admin("admin", "admin")

print(user.authenticate("mypassword")) #True
print(user.authenticate("notmypassword")) #False

#Polymorphism - using same method accross 2 differente classes with a different response.
user.login() #user has logged in
admin.login() #admin has logged in
admin.access_logs() #admin is accessing the logs

