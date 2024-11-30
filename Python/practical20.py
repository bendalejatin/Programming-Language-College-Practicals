#Name: Jatin Bendale
#Enrollment Number: 202203103510038

#Write a python program to copy the content of one file to another file.
file1= open(r"/home/A202203103510038/Documents/python/labpracticals/practical19.txt","r")
file2= open(r"/home/A202203103510038/Documents/python/labpracticals/practical20.txt","w")

for line in file1:
    file2.write(line)
