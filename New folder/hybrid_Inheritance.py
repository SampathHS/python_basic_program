# Python program to demonstrate
# hybrid inheritance


class School:
	def func1(self):
		print("This function is in school class")

class Student1(School):
	def func2(self):
		print("This function is in student 1 class.")

class Student2(School):
	def func3(self):
		print("This function is in student 2 class..")

class Student3(Student1, Student2, School):
	def func4(self):
		print("This function is in student 3 class...")

# Driver's code
object = Student3()
object.func1()
object.func2()
object.func3()
object.func4()
