#  40.	Write a Python program that accepts a string and calculate the number of digits and letters Sample Data :
#  Python 3.2, Expected Output : Letters 6, Digits 2

string = input('Enter any string:  ')

count_alpha = 0
count_digit = 0

for i in range(len(string)):
    if string[i] >= 'a' and string[i] <= 'z' or string[i] >= 'A' and string[i] <= 'Z':
        count_alpha = count_alpha + 1
    elif string[i] >= '0' and string[i] <= '9':
        count_digit = count_digit + 1

print('Number of letters: ',count_alpha, ' , number of digits: ', count_digit)