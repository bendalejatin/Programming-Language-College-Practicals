#Practical : 7- Write a python program to demonstrate the creation of a Dictionary student with 
# the name, age and branch of a student.
# I. Demonstrate the updation of python dictionary.
# II. Demonstrate the removal of elements from the python dictionary.
# III. Demonstrate the use of following dictionary methods - clear(), copy(), get(), items(), 
#  keys(), popitem(), and values(), len() and sorted().

#Dictionary student with the name, age and branch of a student
student={
    "name": "jatin",
    "age" : "18",
    "branch": "CSE"
}

print(student["name"])
print(student["age"])
print(student["branch"])

#Demonstrate the updation of python dictionary.

student.update({"university":"Uka Tarsadia University"})
print(student["university"])

student.update({"date":"8 feb"})
print(student["date"])

#Demonstrate the removal of elements from the python dictionary.

x=student.pop("date")
print(x)

#copy()
a= student.copy()
print(a)

#len()
print(len(student))

#get()
b=student.get("name")
print(b)

#items()
c=student.items()
print(c)

#keys()
d=student.keys()
print(d)

#popitem()
e=student.popitem()
print(e)

#values()
g=student.values()
print(g)

#clear()
f=student.clear()
print(f)

#sorted()
h=student.sorted()
print(h)
