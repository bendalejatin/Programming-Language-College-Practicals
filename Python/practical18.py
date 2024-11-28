#Name: Jatin Bendale
#Enrollment Number: 202203103510038

#Write a python program to demonstrate various regular expressions.
import re

string="We. are Amtics12"
print(string)

# Search for any character (except a newline) in the string (matches the first character)
x=re.search(r'.',string)
print(x)

# Search for a period (.) character in the string
y=re.search(r'\.',string)
print(y)

# Search for the first digit (\d) in the string
v=re.search('\d',string)
print(v)

# Search for a period followed by an "s" (".s") in the string
w=re.search('\.s',string)
print(w)

# Find all occurrences of the letter "A" in the string
z=re.findall('A',string)
print(z)

# Find all occurrences of lowercase letters between "a" and "k"
t=re.findall("[a-k]",string)
print(t)

# Find all occurrences of the word "are"
u=re.findall("are",string)
print(u)

# Find all digit characters in the string
k=re.findall('\d',string)
print(k)

# Check if the string ends with "Amtics12" using '$' (end of string anchor)
l=re.findall("Amtics12$",string)
if l:
  print("Yes, the string ends with 'Amtics12'.")
else:
  print("No match")