#single Inheritance
'''class Baseclass:
    a,b=10,20
    def parent(self):
        print("the addition of two numbers is",self.a+self.b)
class Childclass(Baseclass):
    c,d=30,40
    def Child(self):
        print("the addition of two numbers is",self.c+self.d)
c1=Childclass()
print(c1.c)
print(c1.d)
c1.Child()
print(c1.a)
print(c1.b)
c1.parent()'''
#Multilevel Inheritance
'''class Grandparent:
    a,b=10,20
    def gparent(self):
        print("the addition of two numbers is",self.a+self.b)
class parent(Grandparent):
    m,n=100,20
    def parent(self):
        print("the addition of two numbers is",self.m+self.n)
class Childclass(parent):
    c,d=30,40
    def Child(self):
        print("the addition of two numbers is",self.c+self.d)
c1=Childclass()
print(c1.c)
print(c1.d)
c1.Child()
print(c1.a)
print(c1.b)
c1.gparent()
print(c1.m)
print(c1.n)
c1.parent()'''
#Hirerachial Inheritance
'''class Parent:
    a,b=10,20
    def padd(self):
        print("The addition of two numbers is",self.a+self.b)
class Child1(Parent):
    c,d=30,40
    def coadd(self):
        print("The addition of two numbers is",self.c+self.d)
class Child2(Parent):
    m,n=100,40
    def ctadd(self):
        print("The addition of two numbers is",self.m+self.n)
c2=Child2()
print(c2.m)
print(c2.n)
c2.ctadd()
c2=Child2()
print(c2.a)
print(c2.b)
c2.padd()'''
#multiple Inheritance
'''class Father:
    Desigination="Farmer"
    def fmethod(self):
        print("Father is backbone of family")
class Mother:
    Desigination="Asha worker"
    def mmethod(self):
        print("My mother is Rebel")
class Child(Father,mother):
    Desigination="Waste Fellow"
    def cmethod(self):
        print("care of failure")
c=Child()
c.fmethod()
c.cmethod()'''
#method overriding
'''class A:
    def m1(self):
        print("this is parent method")
class B(A):
    def m1(self):
        print("this is child method")
        super().m1()
b=B()
b.m1()
#overriding the variables
class A:
    a=10

class B(A):
    a=100
    def display(self):
        print(self.a)
b=B()
b.display()'''





