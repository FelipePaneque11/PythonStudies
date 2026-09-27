numbersList = [1,2,3,5,7,9,12,14,16,18,19,20]

#loop through a list and check for numbers bigger than 10
bigNumbers = [bigNumbers for bigNumbers in numbersList if bigNumbers >= 10]
print(bigNumbers)

#Lists Exercise
login_attempts = [3, 5, 1, 6, 9, 2, 8, 10, 3, 12, 4, 15, 1, 2, 6, 8, 4, 7, 20, 5]
#From the list above
#Identify the low activity days. Low activity days are those with login attempts less than 10
#Calculate the average activity using the formula sum(login_attempts) / len(login_attempts)

lowActivityDays = [attempts for attempts in login_attempts if attempts < 10]

def averageActivity():
    return sum(login_attempts) / len(login_attempts)

print(lowActivityDays)
print(averageActivity())