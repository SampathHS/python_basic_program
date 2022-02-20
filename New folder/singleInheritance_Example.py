class Parent():
    def __init__(self,name,regno,branch):
        self.name = name
        self.regno = regno
        self.branch = branch

    def display(self):
        print("Name:", self.name)
        print("Reg_No:", self.regno)
        print("Branch:", self.branch)

class Child(Parent):
    def __init__(self, name, regno,branch):
        Parent.__init__(self,name,regno,branch)
        self.display()
        self.college = 'SIT'
        
  

#obj1 = Parent('Bharathi', 'si19', 'mca')
#obj1.display()

obj2 = Child('Bharathi', 'si19', 'mca')

print("College",obj2.college)
