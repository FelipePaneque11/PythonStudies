import random
import string #manipulates strings

#generates letters(upper and lower case) + digits(numbers) + ponctuations
#Join method puts all the characters together instead having 12 characters separated by a comma.
password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
print(f"Generate password: {password}")
