#with statement - 2 parameters
#there is no need to close the file with the "with" statement
#write to a file
with open("example.txt", "w") as file:
    file.write("Hello World!")

#read the file's content
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

#create a file without with statement
#Close the file is a must!
#file = open("example2.txt", "w")
#file.write("Hello world 2!")
#file.close()