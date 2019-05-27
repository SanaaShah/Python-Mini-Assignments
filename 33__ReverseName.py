#  33.	Write a Python program which accepts the user's first and last name and print them in reverse order with a
#  space between them (Practice After Loops has been discussed)

fname = input('Enter your first name:   ')
lname = input('Enter your last name:    ')


len1 = len(fname)
len2 = len(lname)

i = len1 - 1
j = len2 - 1
rfname = []
rlname = []

for num in range(len1):
    rfname.append(fname[i])
    i = i - 1

for num in range(len2):
    rlname.append(lname[j])
    j = j - 1

print(*rfname, '  ', *rlname)

