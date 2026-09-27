#sets use curly brackets {} while lists uses []
#sets wont allow duplicates
#sets will display items in no particular order
mySet = {"123", "password", "qwerty", "letmein", "123"}
myList = ["123", "password", "qwerty", "letmein", "123"]

print("Set", mySet)
print("List", myList)

print("<----------------------------------------------------->")

#intersection between 2 sets.
set1 = {"192.168.1.101", "10.0.0.1"}
set2 = {"192.168.1.102", "10.0.0.1"}
common_ips = set1 & set2
print("intersection: ", common_ips)

#union between 2 sets.
set3 = {"192.168.1.101", "10.0.0.1"}
set4 = {"192.168.1.102", "10.0.0.1"}
common_ips2 = set3 | set4
print("union: ", common_ips2)

#difference between 2 sets.
set5 = {"192.168.1.101", "10.0.0.1"}
set6 = {"192.168.1.102", "10.0.0.1"}
common_ips3 = set6 - set5
print("Difference: ", common_ips3)

#adding to a set
set6.add("192.168.1.103")
print("adding: ", set6)