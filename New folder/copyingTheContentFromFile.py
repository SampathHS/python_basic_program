
inputFile = open('Student_DetailsNew.txt','r')
outputFile = open('new11_2022.txt', "w")
'''
contentOfTheFile = inputFile.read()
print(contentOfTheFile)
'''
for line in inputFile:
    outputFile.write(line)

print("Successfully copied the content from the file line by line...")

outputFile.close()
