class Animal:
    def eat(self):
        print("animal can eat every thing ")
class Dog(Animal):
    def bark(self):
        print("Among all animal dog can bark")
D1 = Dog()
D1.bark()
D1.eat()