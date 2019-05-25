#  23.	Write a Python program to convert temperatures to and from Celsius, Fahrenheit

temp = input("Enter the  temperature that you want to convert: ")
degree = int(temp[:-1])
ForC = temp[-1]
if ForC.upper() == "C":
    result = int(round((9 * degree) / 5 + 32))
    print('The temperature in Fahrenheit: ' + str(result))

elif ForC.upper() == "F":
    result = int(round((degree - 32) * 5 / 9))
    print('The temperature in Celsius: ' + str(result))
else:
    print("Enter in proper format e.g: 32C or 32F.")
