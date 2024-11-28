#Name: Jatin Bendale
#Enrollment Number: 202203103510038

#Write a python program to demonstrate the use of try-catch block for exception handling.

x=10
try:
    print(x/0)
except:
    print("Zero Divison Error occured!")
print()

#Write a python program to demonstrate the try-finally block.
try:
    print(x)
except:
    print("Something went wrong!")
finally:
    print("Finally, the try except block executed!")
print()

#Write a python program to raise an exception with the python raise keyword.
y=-1
if(y<0):
    raise Exception("Sorry,an error occured!")