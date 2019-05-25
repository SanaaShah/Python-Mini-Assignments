#  3.	Write a Python function to check whether a number is completely divisible by another

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if num1 % num2 == 0:
    print(str(num1)+'  is divisible by  '+str(num2))
elif num2 % num1 == 0:
    print(str(num2)+'  is divisible by  '+str(num1))
else:
    print('They\'re not divisible')
