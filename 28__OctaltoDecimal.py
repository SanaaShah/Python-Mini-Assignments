
deci = int(input('Enter a decimal number:   '))

decimal1, j = 0, 0

while deci != 0:
    dec = deci % 10
    decimal1 = decimal1 + dec * pow(8, j)
    deci = deci//10
    j += 1

print('The Decimal equivalent is: ', decimal1)
