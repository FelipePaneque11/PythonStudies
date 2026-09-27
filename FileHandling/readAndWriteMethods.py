names = ["John\n", "Bob\n", "Marc\n", "Bruno\n"]

with open("names.txt", "w") as file:
    file.writelines(names)

#if it's a big file, we use readline because it will read line by line instead of reading the entire file. Saving memory and processing.
with open("example.txt", "r") as file:
    line = file.readline()
    while line:
        print(line)
        line = file.readline()

with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())