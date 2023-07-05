# que1) Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.
#Ans 
#In object-oriented programming (OOP), a class is a blueprint or a template for creating objects. It defines a set of attributes (data) and methods (functions) that the objects of that class will possess. Essentially, a class encapsulates data and behavior into a single unit.
# for example we get the car model which exist make, model,year,speed 
# my_car = Car("Toyota", "Camry", 2021)
my_car.accelerate(20)
print(my_car.get_speed())  # Output: 20

your_car = Car("Ford", "Mustang", 2019)
your_car.accelerate(30)
print(your_car.get_speed())  # Output: 30

#que 2) Name the four pillars of OOPs.
# pillars of opps
1)Encapsulation
2)inheritance
3)polymorphism
4)abstraction

# que3) Explain why the __init__() function is used. Give a suitable example.
#  Ans 
# the __init__ function is called constructer.is special methos in python classes,
# It is automatically called when an object is created from a class
# the primary purpose of __init__ function is initilize the attributes (data members) of an object with the provided values or default values.
# for ex
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

#que4) Why self is used in OOPs?
# ans 
# Here are a reasons why self is used in OOP
#Differentiating instance variables from local variables
#Adhering to convention
#Supporting polymorphism
#Enabling method chaining

#que5) What is inheritance? Give an example for each type of inheritance.
# Ans 
# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows one class to inherit 
# the properties and behaviors of another class. The class that is being inherited from is called the base class, parent class, or superclass
1) single Inheritance:
In single inheritance, a derived class inherits from a single base class. It represents a one-to-one relationship between classes.
ex 
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

2) Multiple Inheritance:
Multiple inheritance allows a derived class to inherit from multiple base classes. It represents a one-to-many relationship between classes.
ex 
class Bird(Animal, CanFly):
    def chirp(self):
        print(f"{self.name} is chirping.")

3) Multilevel Inheritance:
Multilevel inheritance involves a derived class inheriting from another derived class. It represents a hierarchical relationship between classes.
ex 
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")