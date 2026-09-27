#Write a program that will prompt the user to keep entering a positive number 
#or to type 'done' to exit the program
#As long as the user keeps adding a positive number, we want the program 
#to collect the numbers and put them in a list
#We want the program to check for the first even number 
#and print "the first even number was" and then the number
#Otherwise the program should say "no even numbers found"
#Once the user has decided to exit the program, we want the program to print out 
# all the numbers that were added by the user
#Otherwise the program should say "no numbers were entered"

numbers = []
first_even = None

user_input = input("enter a positive number (or 'done' to exit): ")

while user_input != "done":
    number = int(user_input)
    numbers.append(number)

    if first_even is None and number % 2 == 0:
        first_even = number

    user_input = input("enter a positive number (or 'done' to exit): ")

# after the loop ends (user typed "done")
if first_even is not None:
    print("the first even number was:", first_even)
else:
    print("no even numbers found")

if numbers:
    print("numbers entered:", numbers)
else:
    print("no numbers were entered")
        
        
        
