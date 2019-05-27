#  38.	Write a Python program to get the Fibonacci series between 0 to 50

a, b = 0, 1

for num in range(50):
    print(b)
    a, b = b, a + b
    if b > 50:
        break

