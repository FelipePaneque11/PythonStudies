#challenge 1
#print out a unique IP address

#challenge 2
#look for special ip address {192.168.1.4}

logs = [
    {"username": "alice", "ip": "192.168.1.1", "status": "Success"},
    {"username": "bob", "ip": "192.168.1.2", "status": "Failure"},
    {"username": "alice", "ip": "192.168.1.3", "status": "Failure"},
    {"username": "carol", "ip": "192.168.1.4", "status": "Success"},
    {"username": "bob", "ip": "192.168.1.2", "status": "Failure"},
    {"username": "alice", "ip": "192.168.1.1", "status": "Failure"},
    {"username": "dave", "ip": "192.168.1.5", "status": "Failure"},
    {"username": "bob", "ip": "192.168.1.2", "status": "Failure"},
]

#1
print("1:")
uniqueIp = {log["ip"] for log in logs}
print("Unique IP Addresses: ", uniqueIp)

#2
print("2:")
special_ip = "192.168.1.4"
if special_ip in uniqueIp:
    print("Special IP address -192.168.1.4- was found")
else:
    print("Ip address not found")


#Challenge 3
#count failed login attempts per user
print("3:")
failedAttempts = {}

for log in logs:
    if log["status"] == "Failure":
        username = log["username"]
        if username not in failedAttempts:
            failedAttempts[username] = 0
        failedAttempts[username] += 1

print("Failed login attempts per user: ", failedAttempts)

#challenge 4
#Identify all the unique usernames and print them out
#Count the number of unique IP addresses per user