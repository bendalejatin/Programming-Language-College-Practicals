#Practical : 5- Write a python program to demonstrate the creation of tuples along with its 
# methods - count () and index ().
# I. Demonstrate positive and negative indexing with python Tuple.
# II. Demonstrate slicing operations on python Tuple.

#tuple creation from list and string
a = [1,2,3,4,5,6,7,8]
b =list(a)
b[1]="CSE"
a =tuple(b)
print(a)

a=("AMTICS")#string
print(type(a))
b=("AMTICS",)#tuple
print(type(b))

#tuple created
z=(1,2,3,1,2,1,5,1,5,6,1,1,5,1)
print("Tuple z:",z)

#count()
print(z.count(1))

#index()
print(z.index(4))

#Demonstrate positive and negative indexing with python Tuple.
#Demonstrate slicing operations on python Tuple.

x=(1,2,3,4,5,6,7,8,9,10)
y=("a","b","c","d","e","f")

print("Tuple x:",x)
print("Tuple y:",y)

print(x[-1])
print(x[-6:-1])
print(x[1:5])

print(y[-1])
print(y[-6:-1])
print(y[1:5])
