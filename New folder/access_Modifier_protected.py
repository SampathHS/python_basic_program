class Employee: 
      # constructor 
      def __init__(self, name, sal):
            self._empName = name
            self._empSal = sal

      def display_EmpDetails(self):
            print("Employee Name: ",self._empName)
            print("Employee Salary: ",self._empSal)

emp = Employee('Priyamani', 100000)
print("Employee Name: ",emp._empName)
emp.display_EmpDetails()

# defining a child class 
class HR(Employee): 
      # member function task
      def __init__(self, desig):
            self._designation = desig
                        
      def task(self): 
            print ("We manage Employees")

hrEmp = HR("Captain")

print(hrEmp._designation)

hrEmp.task()

#Accessing unknown members
print(getattr(emp, '_empName'))
print(getattr(hrEmp, '_designation'))
print(getattr(emp, '_empSal'))

# setting an attribute in class Employee
setattr(emp, '_empName', 'Bhavanitha')
print('After modification:', emp._empName)

setattr(hrEmp, '_designation', 'Chief Officer')
print('After modification:', hrEmp._designation)




