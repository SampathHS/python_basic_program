import os.path
import sys

inputFileName = input("Enter name of input file: ")



#Checking for the file existance
if os.path.isfile(inputFileName):
    print(inputFileName, " File already Exists!!!")


    print("Opening file", inputFileName, " for reading.")
    print()

    #opening the input file in the read mode
    inputFile = open(inputFileName, "r")

    #iteratively reading the lines from the input file
    for line in inputFile:
        sys.stdout.write(line)

    #Closing the input file
    inputFile.close()
    print()
    print("Completed reading of file", inputFileName)
else:
    print(inputFileName," file does not exists...")

