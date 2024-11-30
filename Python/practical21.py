#Name: Jatin Bendale
#Enrollment Number: 202203103510038

#Write a python program that creates 26 text files named A.txt, B.txt, and up to Z.txt.
for i in range(65,65+26):
    filename = chr(i) + '.txt'
    file = open(filename,'w')
    file.write(chr(i))