filename = "malware.exe"
if filename[-4:] == ".exe":
    print("it's an executable file")

#endswith is safer as if might not work with shorts like .py 
if filename.endswith(".exe"): 
     print("it's an executable file")

#Using the len function and negative indexes,
#I want you to write a program that will accept a card number = "1234567812345678" 
#and will mask all the characters except the last 4 characters with the "*" symbol.
#Your output must be something like this "Masked: *************5678"
cardNumber = "1234567812345678"
cardLenght = len(cardNumber)
card = cardLenght * "*" 
print(card[:12] + cardNumber[-4:])
#OR
cardNumber = "1234567812345678"
numbOfCharacters = len(cardNumber)
maskedNumber = "*" * (numbOfCharacters-4)
print(maskedNumber + cardNumber[-4:])
