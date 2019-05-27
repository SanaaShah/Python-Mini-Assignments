import  math

hexi = input('Enter a number in HexaDecimal:   ')
result = 0
for i in range(len(hexi)):
    cur_pow = len(hexi) - i - 1
    if hexi[i] == 'A':
        result = result + (10 * math.pow(16, cur_pow))
    elif hexi[i] == 'B':
        result = result + (11 * math.pow(16, cur_pow))
    elif hexi[i] == 'C':
        result = result + (12 * math.pow(16, cur_pow))
    elif hexi[i] == 'D':
        result = result + (13 * math.pow(16, cur_pow))
    elif hexi[i] == 'E':
        result = result + (14 * math.pow(16, cur_pow))
    elif hexi[i] == 'F':
        result = result + (15 * math.pow(16, cur_pow))
    else:
        result = result + (int(hexi[i]) * math.pow(16, cur_pow))

print(result)