#Practical : 19-  Write a python program to read the content of a file and return the number of 
# words in a file to the user.

#Write a python program to read the content of a file and return the number of words in a file to the user.
total_words=0

#Create a text file named practical19.txt to read.
file= open(r"/home/A202203103510038/Documents/python/labpracticals/practical19.txt","r")

data= file.read()
lines= data.split()

total_words += len(lines)

print("Total number of words in this file =",total_words)
