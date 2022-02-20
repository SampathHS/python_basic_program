class Employee: 
      # constructor 
      def __init__(self, name, sal):
            self.empName = name
            self.empSal = sal

      def display_EmpDetails(self):
            print("Employee Name: ",self.empName)
            print("Employee Salary: ",self.empSal)

emp = Employee('Priyamani', 100000)

print("Employee Name: ",emp.empName)

emp.display_EmpDetails()


#Accessing unknown members
print(getattr(emp, 'empName'))
print(getattr(emp, 'empSal'))

# setting an attribute in class Employee
setattr(emp, 'empName', 'Bhanumathi')
print('After modification:', emp.empName)

print(getattr(emp, 'empName'))

print("Employee Name: ",emp.empName)


