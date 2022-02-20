class Employee:
    def __init__(self, n1, id1,d1):
        print("Initializing the constructor of class Employee")
        self.empName = n1
        self.empId = id1
        self.empDept = d1

    def display(self):
        
        print("Employee Name:", self.empName)
        print("Employee Id:", self.empId)
        print("Employee Dept:", self.empDept)
        

class Employee_Details(Employee):
    def __init__(self,n1,id1,d1, p1,s1):
        print("Initializing the constructor of class Employee_Details")
        super().__init__(n1,id1,d1)

        self.empPhoneNo = p1
        self.empSalary = s1
        self.display()

    def display_Child(self):
        print("Employee PhoneNo:", self.empPhoneNo)
        print("Employee Salary:", self.empSalary)
        


obj = Employee_Details('Bharathi', 'si08', 'mca', '1234567890', 75000)
#print(obj)

obj.display_Child()
