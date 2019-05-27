#  42.	Write a Python program to construct the following pattern, using a nested for loop
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(6):
    print()
    for j in range(i):
        print(j+1, end = ' ')
for i in range(4, 0, -1):
    print()
    for j in range(i):
        print(j+1, end = ' ')
