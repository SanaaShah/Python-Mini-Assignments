#  32.	Write a Python program to get the least common multiple (LCM) of two positive integers

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

if num1 > num2:
    greater = num1
else:
    greater = num2
while True:
    if greater % num1 == 0 and greater % num2 == 0:
        lcm = greater
        break
    greater += 1

print('Their LCM is:   ', lcm)