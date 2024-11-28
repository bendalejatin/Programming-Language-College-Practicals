#Practical : 4- Write a python program to demonstrate the creation of List data structure along 
# with its methods - append (), extend(), insert(), remove(), clear(), index(), count(), sort(), 
# reverse(), and copy(),pop(),insert(),min(),max().
# I. Demonstrate positive and negative indexing with python List.
# II. Demonstrate slicing operations on python List.
# III. Demonstrate updation on List elements in python.
# IV. Demonstrate deletion of a single python list element and multiple elements using slicing operator.

#lists
x=[1,2,3]
y=["a","b","c"]
z=["apple",1,2,3,4]

print("List x:",x)
print("List y:",y)
print("List z:",z)

#append()
x.append(y)
print(x)

#extend()
x.extend("4")
print(x)

#insert()
x.insert(0,0)
print(x)

#remove()
x.remove("4")
print(x)

#clear()
z.clear()
print(z)

#index()
print(x.index(3))

#count()
a=[1,2,3,1,2,1,5,1,5,6,1,1,5,1]
print("List a:",a)
print(a.count(1))

#sort()
a.sort()
print(a)

#reverse()
a.reverse()
print(a)

#copy()
c=[1,2,3,4]
print("List c:",c)
d=c.copy()
print(d)

#insert()
c.insert(0,0)
print(c)

#pop()
c.pop(1)
print(c)

#max()
print(max(c))

#min()
print(min(c))

#Demonstrate positive and negative indexing with python List.
#Demonstrate slicing operations on python List.

i=[10,20,30,40,50,60,70,80,90,100]
print("List i:",i)

print(i[2:6])
print(i[:4])
print(i[4:])
print(i[-6:-2])
print(i[-5:-1])
print(c[::-1])

#Demonstrate updation on List elements in python.

list=["apple","banana","mango","orange"]
print("List :",list)
list[0:2]=["watermelon","cherry"]
print(list)
list.insert(0,"banana")
print(list)
list.sort()
print(list)

#Demonstrate deletion of a single python list element and multiple
#elements using slicing operator.

p=['0','1','2','3','4','5','6','7','8']
print("List p:",p)

p.remove('4')
print(p)

p.pop(1)
print(p)

p.clear()
print(p)
