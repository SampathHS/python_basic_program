'''
try:
    f11 = open("copy_2022_224.txt", "r")
except FileNotFoundError: print("File doesnot exist")
else:
    f11.close()
    print(f11.name , " is closed explicitally...")

'''
try:
    variable1="hello"
    print(variable1)
    raise NameError
except NameError:
    print("plz enter correct variable name")





