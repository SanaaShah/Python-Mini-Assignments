#  43.	Write a Python program to construct the following pattern, using a nested loop number.
#
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

for i in range(10):
    print()
    for j in range(i):
        print(i, end='')
