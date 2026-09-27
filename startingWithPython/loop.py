list = ["red", "purple" ,"blue","green" ,"white"]

for l in list:
    print(l, " is a color")
    
counter = 4
while counter > 0:
    print("The value is decreasing")
    counter-=1

numbers = [1,3,5,7,8,9,10,12,14,16,17]
counter = 1
for n in numbers:
    while(n % 2 == 0):
        if(counter == 1):
            print(f"Found the {counter}st even number {n}")
        elif(counter == 2):
            print(f"Found the {counter}nd even number {n}")
        elif(counter == 3):
            print(f"Found the {counter}rd even number {n}")
        else:
            print(f"Found the {counter}th even number {n}")
        counter+= 1
        break