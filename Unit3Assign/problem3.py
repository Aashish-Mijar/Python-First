# 3. Create a 2D list (matrix) of 3 rows and 3 columns. Write a program to display the matrix and calculate the sum of all diagonal elements. 

# 2D matrix 
matrix=[
    [1, 2, 3],    # this is first row 
    [4, 5, 6],    # this is second row 
    [7, 8, 9]     # this is third row 
]

for row in matrix:
    print(row)  # print all matrix 

# sum of diagonal elements
     # first diagonal elements is: 1, 5, 9
first_diagonal = sum(matrix[i][i] for i in range(3))
print("The sum of first diagonal elements:", first_diagonal)

       # second diagonal elements is: 3, 5, 7
second_diagonal = sum(matrix[i][2-i] for i in range(3))
print("The sum of second diagonal elements:", second_diagonal)

# Sum of two diagonal elements
Sum = first_diagonal + second_diagonal
print("The sum of two diagonal elements is :", Sum )