#  13.	Write a Python program that will return true if the two given integer values are equal or their sum or
#  difference is 5.

a = int(input('Enter first number:   '))
b = int(input('Enter second number:  '))

if a == b:
    print('They are equal to 5.')
if abs(a - b) == 5:
    print('Their difference is equal to 5.')
if  (a + b) == 5:
    print('Their sum is equal to 5.')
else:
    print('They are not equal or have sum or difference that is equal to 5.')


