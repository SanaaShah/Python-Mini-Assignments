#  5.	Write a Python program to calculate number of days between two dates

user_input1 = input('Enter first date in format:  dd/mm/yyyy\n')
user_input2 = input('Enter second date in the format:  dd/mm/yyyy\n')
#  we will extract the day, month and year and convert it to integer.
day1 = int(user_input1[0:2])
day2 = int(user_input2[:2])
month1 = int(user_input1[3:5])
month2 = int(user_input2[3:5])
year1 = int(user_input1[6:10])
year2 = int(user_input2[6:10])

#  this is the days each month has
months = [31,28,31,30,31,30,31,31,30,31,30,31]

#  Will calculate total number of days from 00/00/0000 to the first date entered by the user
num1 = year1 * 365 + day1
for i in range(0, month1-1):
    num1 = num1 + months[i]
# calculation of the leap years
if int(month1) <= 2:
    year1 = year1 - 1
leap_year1 = int(year1 / 4 - year1 / 100 + year1 / 400)
num1 = num1 + leap_year1

# similarly we calculate it for the second date entered by the user
num2 = year2 * 365 + day2
for i in range(0, month2-1):
    num2 = num2 + months[i]
if int(month2) <= 2:
    year2 = year2 - 1
leap_year2 = int(year2 / 4 - year2 / 100 + year2 / 400)
num2 = num2 + leap_year2

#  now we can easily find the difference by subtracting num2 which is the total number of days from 00/00/0000 and num1
days =  num2 - num1

print('\nThe difference is: '+str(days))






