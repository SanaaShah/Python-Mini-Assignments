#  41.	Write a Python program to construct the following pattern, using a nested for loop
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(6):
    print()
    for j in range(i):
        print('* ', end = ' ')
for i in range(4,0,-1):
    print()
    for j in range(i):
        print('* ', end = ' ')