class Student:
    'A class representing a student'

    def __init__(self,name,regNumber):
        self.full_name = name
        self.regNumber = regNumber

    def display_regNumber(self):
        return self.regNumber

stud1 = Student('Ram', 21)

#traditional way of accessing the data members...
print(stud1.full_name, stud1.regNumber)


#Accessing unknown members
print(getattr(stud1, 'full_name'))
print(getattr(stud1, 'regNumber'))
#print(getattr(stud1, 'age'))  #AttributeError: 'Student' object has no attribute 'age'


print('~~~~~~~~~~~')
print(getattr(stud1, 'display_regNumber'))  #<bound method Student.display_regNumber
#of <__main__.Student object at 0x000001667BB91D90>>

#Accessing unknown member function ()
print(getattr(stud1, 'display_regNumber')())

setattr(stud1, 'full_name', 'Ravi...')
print('After modification:', stud1.full_name)

# setting an attribute not present in class Student
setattr(stud1, 'age', 23)
print('Age is:', stud1.age)

setattr(stud1, 'branch', 'MCA')
print('Branch:', stud1.branch)

print(getattr(stud1, 'age'))
print(getattr(stud1, 'branch'))

print(hasattr(stud1,'full_name'))
print(hasattr(stud1,'regNumber'))
print(hasattr(stud1,'age'))

stud2 = Student('Priyamani', 18)
print(getattr(stud2, 'full_name'))
print(getattr(stud2, 'regNumber'))
print(getattr(stud2, 'age'))  #AttributeError: 'Student' object has no attribute 'age'
print(getattr(stud2, 'branch')) #AttributeError: 'Student' object has no attribute 'branch'

print(hasattr(stud2,'full_name'))
print(hasattr(stud2,'regNumber'))
print(hasattr(stud2,'age'))
