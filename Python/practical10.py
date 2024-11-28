#Practical : 10- Write a python program to demonstrate the use of user-defined functions with single, 
# multiple and arbitrary arguments.WAP to design simple calculator

# returns sum of a and b
def Add(a, b):
    return a + b

# return subtraction of a and b
def Subtract(a,b):
    return a - b

# returns Multiply of a and b
def Multiply(a, b):
    return a * b

# return Divide of a and b
def Divide(a,b):
    return a / b

print("Select operation -" 
        "\n1. Add" 
        "\n2. Subtract" 
        "\n3. Multiply" 
        "\n4. Divide\n")

select = int(input("Select operations from 1, 2, 3, 4 :"))
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",Add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",Subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",Multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=",Divide(number_1, number_2))
else:
    print("Invalid input")
