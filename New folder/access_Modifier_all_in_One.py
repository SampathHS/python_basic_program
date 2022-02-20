# define parent class Company
class Company:
    # constructor
    def __init__(self, name, proj):
        self.name = name      # name(name of company) is public
        self._proj = proj     # proj(current project) is protected
    
    
# define child class Emp
class Emp(Company):
    # constructor
    def __init__(self, eName, sal, cName, proj):
        # calling parent class constructor
        Company.__init__(self, cName, proj)
        self.name = eName   # public member variable
        self.__sal = sal    # private member variable
    
    # public function to show salary details
    def show_sal(self):
        print("The salary of ",self.name," is ",self.__sal,)

# creating instance of Company class
c = Company("TCS", "COVID-19")
# creating instance of Employee class
e = Emp("Radha", 1000000, c.name, c._proj)

print("Welcome to ", c.name)
print("Here",e.name,"is working on",e._proj)

# to show the value of __sal we have created a public function show_sal()
e.show_sal()
