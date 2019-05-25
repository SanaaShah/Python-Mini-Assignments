#  10.	Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

number = input('Enter any number: ')
if int(number) % 2 == 0:
    print('This number is even: '+number)
else:
    print('This number is odd: '+number)

