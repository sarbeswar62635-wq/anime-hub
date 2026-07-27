class Employee:
     company = "HP"
     def __init__(self,name,salary):
        self.name = name
        self.salary = salary
     def __str__(self):
         return f"the name is {self.name} and salary is {self.salary}"
     def __repr__(self):
         return f"name:{self.name}\nsalary:{self.salary}"
e = Employee("sahoo",3000000)
print(e.name,e.salary)
print(str(e))
print(repr(e))