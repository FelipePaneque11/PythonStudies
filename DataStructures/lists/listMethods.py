numbers = [1,2,3,4,5]
newList = [6,7,8,9]
#add something to the list
newList.append(10)

#extend a list into another
numbers.extend(newList)
print(numbers)

#remove from list
numbers.remove(4)
print(numbers)

#reverse
numbers.reverse()
print(numbers)

#clear list
numbers.clear()
print(numbers)