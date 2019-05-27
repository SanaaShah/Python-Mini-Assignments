#  26.	Write a Python program to convert an integer to Binary, Octal and Hexadecimal numbers

num = int(input('Enter a decimal number:   '))
save = num
save1 = num

#  this is calculated using built in methods of python

print('Its Binary is:       ', bin(num))
print('Its Octal is:        ', oct(num))
print('Its hexadecimal is:  ', hex(num))

#  now calculating the values manually for practice

lst = []
while num > 0:
    a = int(float(num%2))
    lst.append(a)
    num = (num-a)/2
lst.append(0)
string = ""
for j in lst[::-1]:
    string = string+str(j)
print('\nThe binary is:  ', string)

octal = 0
multiplier = 1

while save > 0:
    octal = int(octal + (save % 8) * multiplier)
    save = int(save / 8)
    multiplier = multiplier * 10

print('Octal is:  ', (octal))

hex_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
reversed_number = ""
while save1 > 0:
    remainder = save1 % 16
    save1 -= remainder
    save1 //= 16
    reversed_number += str(hex_values[remainder])

print("Hexadecimal number is : ", reversed_number[::-1])





