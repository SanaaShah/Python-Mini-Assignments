#  25.	Write a Python program to calculate the sum of the digits in an integer

inp = input('Enter any integer:   ')
num = len(inp)


arr = []
sum = 0

for i in range(0, num):
    arr.append(inp[i:i+1])

for i in range(0, num):
    sum = sum + int(arr[i])

print('The sum of digits is:  '+str(sum))