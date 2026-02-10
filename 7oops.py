# class Car:
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color

#     def start(self):
#         print(f"{self.color}{self.brand} is starting...")

# car1 = Car("Tesla ", "Red ")
# car2 = Car("BMW ","Black ")

# car1.start()
# car2.start()


# class Employee:
#     company = "TechCorp"    #Class variable

#     def __init__(self,name,salary):
#         self.name=name      #Instance variable
#         self.salary=salary

# e1= Employee("John",50000)
# e2= Employee("Emma",60000)
# e3= Employee("Atul",70000)

# print(e1.company)
# print(e2.salary)
# print(e3.company)
# print(e3.name,e3.salary)


# class Animal:
#     def speak(self):
#         print("Animal Make sound")
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks! ")

# d=Dog()
# d.speak()
# d.bark()


# class Animal:
#     def sound(self):
#         print("Some generic sound")

# class Cat(Animal):
#     def sound (self):
#         print("Meow! ")

# a=Animal()
# c=Cat()
# a.sound()
# c.sound()


# class Student:
#     def __init__(self,Name,Roll_no,Makrs):
#         self.Name=Name
#         self.Roll_no=Roll_no
#         self.Marks=Makrs
#     def details(self):
#         print(f"{self.Name},{self.Roll_no}{self.Marks}")

# Student1=Student("Abhishek","29 ","85%")
# student2=Student("Abhay","13 ","82%")
# student3=Student("Abhishek Rajpoot","27 ","92%")

# Student1.details()
# student2.details()
# student3.details()


# class Circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         print("Area of Circle:",3.14*self.radius*self.radius)
#     def circumference(self):
#         print("Circumference of Circle:",2*3.14*self.radius)

# cir1=Circle(5)
# cir2=Circle(9)
# cir3=Circle(102)

# cir1.area()
# cir2.circumference()
# cir3.area()
# cir1.circumference()


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(person):
    def __init__(self,name,age, salary):
       super().__init__(name,age)
       self.salary=salary
    def display(self):
        print(self.name,self.age,self.salary)
        

emp1=Employee("Abhimanyu", 28,60000)
emp2=Employee("Vinay",27,85000)
emp3=Employee("Anurag",60000,50000)

emp1.display()
emp2.display()
emp3.display()