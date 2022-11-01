# class Person:
#     a=10 #class level variable
#     def display(self):
#         print(self.a)
# p1=Person()
# p1.display()
#Example 2
# class person:
#     name="Tharun"
#     age=20
#     city="Chittoor"
#     def display(selfs):
#         print("my name is ",selfs.name)
#         print("my age is ",selfs.age)
#         print("my city is ",selfs.city)
# p1=person()
# p1.display()
#Example3
# class Details:
#     def __init__(self,name,age,city):
#         self.name=name
#         self.age=age
#         self.city=city
#     def display(self):
#         print("My name is ",self.name)
#         print("My age is ", self.age)
#         print("My city is ", self.city)
# D=Details("tharun",21,"Chittoor")
# print(D.display())
#instance method example
# class Details:
#     def __init__(self,name,age,city):
#         self.name=name
#         self.age=age
#         self.city=city
#     def display(self):
#         print("My name is ",self.name)
#         print("My age is ", self.age)
#         print("My city is ", self.city)
# D=Details("tharun",21,"Chittoor")
# D.display()
#Static method
# class Details:
#     def display(self):
#         print("Instance method..")
#     @staticmethod
#     def show(self):
#         print("Static method")
# d=Details()
# d.display()
# Details.show("None")
# class Details:
#     name="tharun"
#     def __init__(self):
#         name="Deepikr"
#         print(name)
#     @staticmethod
#     def display(self):
#         print(self.name)
# d=Details()
#Details.display(1)
class Add:
  @staticmethod
  def addition(a,b):
    print(a+b)
a=Add()
a.addition(10,20)