#  2.	Write a Python program to check if a number is positive, negative or zero

user_input = float(input('Please enter any number: '))

if user_input < 0:
    print('Entered number is negative.')
elif user_input > 0:
    print('Entered number is positive')
elif user_input == 0:
    print('You have entered zero, its neither negative nor positive')
