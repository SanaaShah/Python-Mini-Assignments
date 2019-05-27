#  24.	Write a python program to sum of the first n positive integers

num = int(input('Please enter the number'
                ' that you want to sum:  '))
sum = 0
for i in range(0, num+1, 1):
    sum = sum+i

print("The sum is found to be:   ", sum)


