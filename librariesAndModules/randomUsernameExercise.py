import random
import string 

def generate_username():
    first_two_upp = "".join(random.choices(string.ascii_uppercase, k=2))
    four_random_low = "".join(random.choices(string.ascii_lowercase, k=4))
    last_two_digits = "".join(random.choices(string.digits, k=2))
    
    password = first_two_upp + four_random_low + last_two_digits
    return password



print(generate_username())