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


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Employee(person):
#     def __init__(self,name,age, salary):
#        super().__init__(name,age)
#        self.salary=salary
#     def display(self):
#         print(self.name,self.age,self.salary)
        

# emp1=Employee("Abhimanyu", 28,60000)
# emp2=Employee("Vinay",27,85000)
# emp3=Employee("Anurag",60000,50000)

# emp1.display()
# emp2.display()
# emp3.display()


#Encapsulation

# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.__balance=balance   #Private attribute

#     def deposite(self,amount):
#         self.__balance+=amount

#     def get_balance(self):
#             return self.__balance
        
# acc=BankAccount("Alice",10000)
# acc.deposite(5000)
# print(acc.get_balance())


# class Student:
#     def __init__(self,marks):
#         self.__marks=marks     #Private attributes
    
#     def display(self):
#         print(self.__marks)
    
# st1=Student(84)
# st2=Student(94)

# st1.display()
# st2.display()


# class Employee:
#     def __init__(self,salary):
#         self.__salary=salary

#     def inc(self,amount):
#         self.__salary+=amount

#     def get_balance(self):
#         print(self.__salary)

# rs=Employee(10000)
# rs.inc(50000)
# print(rs.get_balance())


# class Account():
#     def __init__(self,balance):
#         self.__balance=balance
#     def balance(self,deposite):
#         self.__balance+=deposite
#     def get_display(self):
#         print(self.__balance)

# s1=Account(4102)
# s1.balance(7823)
# print(s1.get_display())


# class Mobile():
#     def __init__(self,price):
#         self.__price=price
    
#     def set_price(self,new_price):
#         self.__price+= new_price

#     def get_price(self):
#         return self.__price

# rs1=Mobile(5000)
# rs1.set_price(2480)
# print(rs1.get_price())


# class person():
#     def __init__(self,age):
#         self.__age=age

#     def show_age(self):
#         print(self.__age)

# st1=person(27)
# st1.show_age()


# class car():
#     def __init__(self,speed):
#         self.__speed=speed
#     def set_inc(self,new_spe):
#         self.__speed+=new_spe
#     def get_val(self):
#         return self.__speed
    
# sp=car(50)
# sp.set_inc(20)
# print(sp.get_val())    


#instance variable
class Company():
    company_name="INFOSYS"

    def __init__(self,employee_name):
        self.employee_name=employee_name

em1=Company("Alice")
em2=Company("Abhishek")

print(em2.company_name)
print(em1.employee_name,em1.company_name)