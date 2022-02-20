class Employee: 
      # constructor 
      def __init__(self, name, sal):
            self.__empName = name
            self.__empSal = sal

      def display_EmpDetails(self):
            print("Employee Name: ",self.__empName)
            print("Employee Salary: ",self.__empSal)

emp = Employee('Priyamani', 100000)

#First execute the code, it raises with excepection...
#then comment the below line and execute...
print("Employee Name: ",emp.__empName)


emp.display_EmpDetails()


#Accessing unknown members
print(getattr(emp, '__empName'))
print(getattr(emp, '__empSal'))



