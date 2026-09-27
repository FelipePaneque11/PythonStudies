username = input("enter your username: ")

# "a" parameter means "append" - meaning whatever we write, wont be overwritten
with open("users.txt", "a") as file:
    #\n means new line
   file.write(username + "\n")

print("username has been added to the file")

with open("users.txt", "r") as file:
    for index,name in enumerate(file, start=1):
        #strip() cuts off spaces
        print(f"Username {index}: ", name.strip())