#  31.	Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

if num1 > num2:
    num1, num2, = num2, num1

for i in range(num1, 0, -1):
    if num1 % i==0 and num2 % i == 0:
       result = i
       break

print('Their GDC is:  ', result)

