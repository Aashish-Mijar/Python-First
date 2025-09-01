
matrix=[
    [1, 2, 3],    # this is first row (index 0)
    [4, 5, 6],    # this is second row (index 1)
    [7, 8, 9]     # this is third row (index 2)
]


print("matrix:", matrix)
print(matrix[0])   # print first row

print(matrix[0][0])  #print first value in first row 
print(matrix[0][1])
print(matrix[0][2])
print(matrix[1][0])
print(matrix[1][1])
print(matrix[1][2])
print(matrix[2][0])
print(matrix[2][1])
print(matrix[2][2]) #print last value in last row


print("Now print all value using for loop")
# This program can use for loop to print all value in matrix:
    
for row in matrix:
    for item in row:
        print(item)