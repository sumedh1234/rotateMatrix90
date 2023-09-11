matrix = [[1,2,3],[4,5,6],[7,8,9]]
row = len(matrix)
col = len(matrix[0])
print()
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end = ' ')
    print()
print()
print("--Rotated by 90 degree--")
print()
for i in range(row):
    for j in range(col-1,-1,-1):
        print(matrix[j][i], end = ' ')
    print()
print()