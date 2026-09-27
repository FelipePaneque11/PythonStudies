numberToGuess = 25
listOfGuesses = "10, 23, 25 ,30, 45, 56, 77, 81, 99"

print("Try to guess the number: " + listOfGuesses)

while True:
    try:
        userGuess = int(input())
        if userGuess == numberToGuess:
            print("Congratulations! You've guessed the number! and ended the game.")
            break
        elif userGuess < numberToGuess:
            print("Too low! Try again.")
        elif userGuess > numberToGuess:
            print("Too high! Try again.")
            continue
    except ValueError:
        print("Enter a valid number")