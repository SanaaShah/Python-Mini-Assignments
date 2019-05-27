#  35.	Write a Python program to find the number of notes (Sample of notes: 10, 20, 50, 100, 500, and 1000 )
#  against an given amount

inp = int(input('Enter any number to find the notes:  '))

notes = [500, 200, 100, 50, 20, 10]
ans = 0
for i in range(6):
    num = notes[i]
    ans += int(inp / num)
    inp = int(inp % num)
if inp > 0:
    ans = -1

print('The number of notes are:  ', ans)
