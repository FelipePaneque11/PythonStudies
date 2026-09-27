import random #random numbers

letters = "abcdefghijklmnopqrstuvwxyz"
#choice() returns one char
random_letter = random.choice(letters)
print(f"random letter chosen is: {random_letter}")

#choices() needs 2 parameters, and returns more than 1 
random_letters = random.choices(letters, k=3)
print(f"random letters chosen is: {random_letters}")
