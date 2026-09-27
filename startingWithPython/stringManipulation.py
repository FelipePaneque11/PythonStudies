#admin@domain.com
#https://website.com/path/to/file

email = "admin@domain.com"
name = email.split("@")[0]
domain = email.split("@")[1]
print(name)
print(domain)

url = "https://website.com/path/to/file"
filename = url.split("/")[-1]
print(filename)

username = email[:email.index("@")]
domain1 = email[email.index("@") + 1:]
print("username: ", username)
print("domain: ", domain1)

#Given an email string, perform string operations to:
#Extract the username and domain.
#Convert the username to uppercase.
#Display the first letter of the domain followed by *** for privacy.
#The email string should be "user@labcyber.com"
email = "user@labcyber.com"

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

usernameUpper = username.upper()
usernameLen = len(username) 
print(usernameUpper[0] + (usernameLen - 2) * "*" + usernameUpper[-1:])