from datetime import datetime
import random

actions = ["login", "logout", "registration", "reset_password"]

current_time = datetime.now()
user_action = random.choice(actions)

print(f"the user performed a {user_action} at {current_time}")
