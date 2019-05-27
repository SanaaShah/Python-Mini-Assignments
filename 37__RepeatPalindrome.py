#  37.	Write a Python program to reverse the digits of a given number and add it to the original, If the sum is not a
#  palindrome repeat this procedure

num = int(input('Enter a number:  '))
sum = 0
while True:
    i = str(num)
    if i == i[::-1]:
        break
    else:
        j = int(i[::-1])
        num += j
        sum += 1

print(num, '  is a palindrome.')
