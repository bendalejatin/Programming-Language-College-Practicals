#Name: Jatin Bendale
#Enrollment Number: 202203103510038

#Assignment operations
print("###Assignment operations###")

a=int(input("Enter the 1st number:"))

b=a
print("=:",b)
b+=a
print("+=:",b)
b-=a
print("-=:",b)
b*=a
print("*=:",b)
b/=a
print("/=:",b)
b%=a
print("%=:",b)
c=int(input("Enter the 1st number:"))
c//=a
print("//=:",b)
c**=a
print("**:",b)
d=int(input("Enter the 1st number:"))
d<<a
print("<<:",b)
d>>a
print(">>:",b)
d^=a
print("^=:",b)
d|=a
print("|=:",b)
d&=a
print("&=:",b)

#Arithmetic operations
print("###Arithmetic operations###")

a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))

add=a+b
print("Addition:",add)
sub=a-b
print("Subtraction:",sub)
mul=a*b
print("Multiplication:",mul)
div=a/b
print("Division:",div)
flr=a//b
print("Floor Division:",flr)
mod=a%b
print("Modulus:",mod)
exp=a**b
print("Exponent:",exp)

#Logical operations
print("###Logical operations###")

a=9
print("and operator:",a < 5 and  a < 10)
print("or operator:",a < 5 or a < 4)
print("not operator:",not(a < 5 and a < 10))

#Comparison/Relational operations
print("###Comparison/Relational operations###")

a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))

print("greater than:",a>b)
print("less than:",a<b)
print("Equal to:",a==b)
print("not equal to:",a!=b)
print("greater than equal to:",a>=b)
print("lesser than equal to:",a<=b)

#Bitwise operations
print("###Bitwise operations###")

a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))

print("Bitwise AND:",a&b)
print("Bitwise OR:",a|b)
print("Bitwise NOT:",~a)
print("Bitwise XOR:",a^b)
print("Bitwise right shift:",a>>b)
print("Bitwise left shift:",a<<b)

#Identity operations
print("###Identity operations###")

a=input("Enter the 1st number:")
b=input("Enter the 2nd number:")

print("is:",a is b)
print("is not:",a is not b)

#Membership operations
print("###Membership operations###")

x = "Hello world"
print('H' in x)
print('Hello' not in x)
print("hello" in x)