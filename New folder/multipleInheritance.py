class Personal_info:
    def __init__(self,name,regno,place):
        self.name=name
        self.regno=regno
        self.place=place

class Acadamic_info:
    def __init__(self,dept,year):
        self.dept=dept
        self.year=year

class Student_information(Personal_info,Acadamic_info):
    def __init__(self,name,regno,place,dept,year,marks):
        Personal_info.__init__(self,name,regno,place)
        Acadamic_info.__init__(self,dept,year)
        self.marks=marks

    def display(self):
        print("Student information")
        print("Name:",self.name)
        print("Regno:",self.regno)
        print("Place:",self.place)
        print("Department:",self.dept)
        print("Year:",self.year)
        print("Student result")
    
        for i in marks:
            if(i <35):
                print("Fail!!!!")
                break
            else:
                print("Pass")


print("Enter student details:")
name=input("Enter student name :")
regno=input("Enter student regno:")
place=input("Enter student place:")
dept=input("Enter student department:")
year=input("Enter student year:")
marks=[]
noOfSub=int(input("Enter no subjects"))

print("Subjects:",noOfSub)

for i in range(noOfSub):
   mark=int(input("Enter marks")) 
   marks.append(mark)
print("marks",marks)


student1 = Student_information(name,regno,place,dept,year,marks)
student1.display()




