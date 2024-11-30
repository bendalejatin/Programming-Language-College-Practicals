#Practical : 21- Write a python program that creates 26 text files named A.txt, B.txt, and up to Z.txt.

#Write a python program that creates 26 text files named A.txt, B.txt, and up to Z.txt.
for i in range(65,65+26):
    filename = chr(i) + '.txt'
    file = open(filename,'w')
    file.write(chr(i))

# This program will create 26 text files in the folder in which this file is executed.
