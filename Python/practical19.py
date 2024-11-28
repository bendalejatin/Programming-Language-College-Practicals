#Name: Jatin Bendale
#Enrollment Number: 202203103510038

#Write a python program to read the content of a file and return the number of words in a file to the user.
total_words=0

file= open(r"/home/A202203103510038/Documents/python/labpracticals/practical19.txt","r")

data= file.read()
lines= data.split()

total_words += len(lines)

print("Total number of words in this file =",total_words)