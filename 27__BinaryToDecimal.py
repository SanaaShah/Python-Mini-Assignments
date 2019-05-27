#  27.	Write a program to convert binary number to Decimal number

binary = int(input('Enter a binary number:   '))
decimal, i = 0, 0

while binary != 0:
    dec = binary % 10
    decimal = decimal + dec * pow(2, i)
    binary = binary//10
    i += 1

print('The Decimal equivalent is: ', decimal)

