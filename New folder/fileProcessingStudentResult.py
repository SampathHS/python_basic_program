

inputFile = open("Student_DetailsResult.txt", "r")

print ("Reading from file input.txt")
print("--------------------- ************************** ------------------------")

for line in inputFile:
    resultFlag = 'Pass'
    name,semester,college,sub1,sub2,sub3,sub4,sub5 = line.split(',')
    last,first = name.split()
    
    print("Name: %s, %s\tSemester: %s\tCollege: %s\nSubject1: %s \tSubject2: %s \tSubject3: %s \tSubject4: %s \tSubject5: %s" 
             %(last,first,semester,college,sub1,sub2,sub3,sub4,sub5 ))

    if int(sub1) < 40:resultFlag = 'Fail'
    if int(sub2) < 40:resultFlag = 'Fail'
    if int(sub3) < 40:resultFlag = 'Fail'
    if int(sub4) < 40:resultFlag = 'Fail'
    if int(sub5) < 40:resultFlag = 'Fail'

    print("Name: %s, %s\tResult: %s"%(last,first,resultFlag))
    print()
    print("+" * 73, "\n")
    
print("--------------------- ************************** ------------------------")
print ("Completed reading of file input.txt")
inputFile.close()
