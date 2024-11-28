#Name: Jatin Bendale
#Enrollment Number: 202203103510038

#sets
a={1,2,3,4,5,"abc"}
b={"x","y","z"}
c=[1,2]

for x in a:
    print(x)

#add()
a.add("xyz")
print(a)

#clear()
a.clear()
print(a)

#update()
a.update(c)
print(a)

a.update(b)
print(a)

#deleting methods
a.remove("x")
print(a)

a.discard("y")
print(a)

a.pop()
print(a)

del(a)

x={"a","b","c",1}
y={1,2,3}

#union()
p=x.union(y)
print(p)

#intersection()
q=x.intersection(y)
print(q)
x.intersection_update(y)
print(y)

r=x.symmetric_difference(y)
print(r)
x.symmetric_difference_update(y)
print(x)

s={1,2,3,4,5,6}
t={1,3,5}

#issubset
print(t.issubset(s))

#issuperset()
print(s.issuperset(t))

#isdisjoint
print(s.isdisjoint(t))

a={1,2,3,4,5,"abc"}
s1=list(a)
print(s1)
print(type(s1))
s2=tuple(s1)
print(s2)
print(type(s2))
s3=set(s2)
print(s3)
print(type(s3))