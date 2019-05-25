#  7. Write a Python program to get the difference between a given number and 17, difference cannot be negative

num = int(input('Enter a number:  '))
if num <= 17:
  diff = 17 - num
else:
    diff = (num - 17) * 2

print('Difference: '+ str(diff))
