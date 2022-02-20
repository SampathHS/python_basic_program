'''
try:
	fileEx_Handling = open("copy_new12.txt", "w") 
	fileEx_Handling.read() 
except IOError: print("Error: can\'t find", fileEx_Handling, "file")
else:
        print("No exception has occured" )

        fileEx_Handling.close()

'''
import os
checkingInputFile = True
while checkingInputFile:
        try:
                #if you comment the below line, checkingInputFile will be "True" always
                checkingInputFile = False
                filename = input("Enter a filename: ").strip()
                
                if os.path.isfile(filename):
                        infile = open(filename, "r") # Open the file
                        print("The file content is...\n", infile.read())
                else:
                        raise IOError
                        
        except IOError:
            print("File " + filename + " does not exit")
            break


