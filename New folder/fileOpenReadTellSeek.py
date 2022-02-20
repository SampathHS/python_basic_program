#!/usr/bin/python

# Open a file
infile = open("python.txt", "r+")

mystr = infile.read(30);
print("String after Reading : ", mystr)

# Check current position
position = infile.tell();
print("Current file position : ", position)

# Reposition pointer at the beginning once again
#with seek() for from argument value to 0
position = infile.seek(0, 0)
mystr1 = infile.read(10)
print("String after Reading Again :", mystr1)

# Reposition pointer to the current position once again
#with seek() for from argument value to 1
position = infile.seek(0, 1)
mystr1 = infile.read(15)
print("String after Reading Again :", mystr1)

# Reposition pointer to the end position 
#with seek() for from argument value to 2
position = infile.seek(0, 2)
mystr1 = infile.read(15)
print("String after Reading Again :", mystr1)

# Close opend file
infile.close()
