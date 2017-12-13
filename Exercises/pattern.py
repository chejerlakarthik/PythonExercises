limit = 120
col1 = 20
col2 = 40
header = 10
matrix = [[' ' for x in range(limit)] for y in range(limit)]

for x in range(limit):
    for y in range(limit):
        if x in (0,header, limit-1):
            matrix[x][y] = '-'
        if y in (0,col1, col2,limit-1):
            if y == limit-1:
                matrix[x][y] = '|\n'
            else:
                matrix[x][y] = '|'
        
with open('pattern.txt', 'w+') as file:
    for x in range(limit):
        for y in range(limit):
            file.write(matrix[x][y])
