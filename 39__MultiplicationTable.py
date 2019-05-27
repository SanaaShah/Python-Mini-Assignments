#  39.	Write a Python program to create the multiplication table (from 1 to 10) of a number

num = int(input('Enter any number to print its multiplication table:  '))

for i in range(10):
    print(num, ' X ', i+1, ' = ' , num*(i+1))


