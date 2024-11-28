#Practical : 9- Write a python program to display above patterns.
#Pattern 1
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

#Pattern 2
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

#Pattern 3
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

#Pattern 4
# A
# B B
# C C C
# D D D D
# E E E E E

#Pattern 1
print("Pattern 1:")
rows=5
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
print()

#Pattern 2
print("Pattern 2:")
num=1
rows=5
k=2
for x in range(rows):
    for y in range(1,k):
        print(num, end=" ")
        num +=1
    print()
    k+=1
print()

#Pattern 3
print("Pattern 3:")
k=4
for i in range(0,5):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print()
print()

#Pattern 4
print("Pattern 4:")
num=65
for i in range(0,5):
    for i in range(0,i+1):
        c = chr(num)
        print(c, end=" ")
    num+=1
    print()
print()
