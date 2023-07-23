import math
def pattern(n, whitespace):
    ''' This function generates a string pattern of size n
    if n =3, then a-b-c pattern will be generated and returned
    '''
    ascii = 96
    str = ""
    for i in range(1, n+1):
        if i == n:
            str += chr(ascii + i)
        else:
            str += chr(ascii + i) + whitespace
    return str

n = int(input())
whitespace = "-"
str_pattern = pattern(n, whitespace)[::-1]

#iterate and store the each pattern in a list
firsthalf_pattern = []

l = len(str_pattern)
for i in range(1, math.ceil(l/2) + 1):
    temp = whitespace*(l - (2*i -1)) + str_pattern[:(2*i -1)]
    firsthalf_pattern.append(temp + temp[:-1][::-1])

for pattern in firsthalf_pattern:
    print(pattern)

#print second half
for i in range(len(firsthalf_pattern)-2, -1, -1):
    print(firsthalf_pattern[i])
   

