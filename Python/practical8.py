#Name: Jatin Bendale
#Enrollment Number: 202203103510038

#if-else:- Python program to check whether the string is Symmetrical or Palindrome
#Python program to check whether the string is Symmetrical
def palin(string): 
    start = 0
    end = len(string)-1
    f = 0
    while(start<end): 
        if (string[start]== string[end]): 
            start += 1
            end -= 1
        else: 
            f = 1
            break;   
    if f == 0: 
        print("The entered string is palindrome") 
    else: 
        print("The entered string is not palindrome") 
string = input("Enter the string: ")
palin(string)
print()
    
#Python program to check whether the string is Palindrome
def symm(string): 
    length = len(string) 
    flag = 0
    if length%2 == 0: 
        mid = length//2 
    else: 
        mid = length//2 + 1     
        s1 = 0  
        s2 = mid 
    while(s1 < mid and s2 < length):  
        if (string[s1] == string[s2]): 
            s1 = s1 + 1
            s2 = s2 + 1
        else: 
            flag = 1
            break 
    if flag == 0: 
        print("The entered string is symmetrical") 
    else: 
        print("The entered string is not symmetrical") 
string = input("Enter the string: ")
symm(string)
print()

#for() - Program to multiply two matrices using nested loops.
#matrix A
r1=int(input("Enter no. of rows of matrix A: "))
c1=int(input("Enter no. of columns of matrix A: "))
A=[[0 for i in range(c1)] for j in range(r1)]
print("Enter the elements of matrix A")
for i in range(r1):                               
    for j in range(c1): 
        x=int(input())
        A[i][j]=x
print(A)

#matrix B
r2=int(input("Enter no. of rows of matrix B: "))
c2=int(input("Enter no. of columns of matrix B: "))
B=[[0 for i in range(c2)] for j in range(r2)]
print("Enter the elements of matrix B")
for i in range(r2):                    
    for j in range(c2): 
        x=int(input())
        B[i][j]=x
print(B)

#multiplication of both matrices
result=[[0 for i in range(c2)] for j in range(r1)]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)): 
                   result[i][j] += A[i][k] * B[k][j]
print("The final matrix is:")
for r in result:
    print(r)
print()

#reverse of a string
string=input("Enter a string: ")
l=len(string)
i=string
reverse=""
while(len(i)>0):
    a = i[-1]
    i = i[:-1]
    reverse += a
print(reverse)