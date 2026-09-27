user_info = {
    "username" : "admin",
    "password": "1234",
    "last_login": "2024-10-22"
}

#adding a new property to the dictionary
user_info["email"] = "admin@admin.com"
#updating 
user_info["password"] = "4321"
#retrive a information
print("username: " + user_info.get("username"))
#getting the keys
print("keys: ",  user_info.keys())
#getting the values
print(f"values:  {user_info.values()}")
print(user_info)

print("------------------------------------------------loop")
for key, value in user_info.items():
    print(f"{key}: {value}")