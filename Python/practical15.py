#Practical : 15- Write a python program to perform basic matrix operations on user entered matrices.

# matrix multiplication function
def matrix_multiply(a, b):
    r1, c1 = len(a), len(a[0])
    r2, c2 = len(b), len(b[0])
    if c1 != r2:
        return "Matrices cannot be multiplied"

    result = [[0 for _ in range(c2)] for _ in range(r1)]

    # iterate through each row in matrix1
    for i in range(r1):
        # iterate through each column in matrix2
        for j in range(c2):
            # iterate through each element in the corresponding row and column
            for k in range(c1):
                result[i][j] += a[i][k] * b[k][j]

    return result

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
matrix1 = []
print("Enter the entries rowwise:")

# For user input
for i in range(R):		 # A for loop for row entries
	a =[]
	for j in range(C):	 # A for loop for column entries
		a.append(int(input()))
	matrix1.append(a)

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

matrix2 = []
print("Enter the entries rowwise:")

# For user input
for i in range(R):		 # A for loop for row entries
	a =[]
	for j in range(C):	 # A for loop for column entries
		a.append(int(input()))
	matrix2.append(a)

result = matrix_multiply(matrix1, matrix2)
print("Multiplication of two matrices is:")
for rows in result:
    for element in rows:
        print(element,end=" ")
    print()
