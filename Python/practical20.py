#Practical : 20- Write a python program to copy the content of one file to another file. 

#Write a python program to copy the content of one file to another file.

#Create a text file named practical19.txt to read.
file1= open(r"/home/A202203103510038/Documents/python/labpracticals/practical19.txt","r")
#Create a text file named practical20.txt to write.
file2= open(r"/home/A202203103510038/Documents/python/labpracticals/practical20.txt","w")

for line in file1:
    file2.write(line)
