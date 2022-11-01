'''a,b=10,20
class Variables:
    a,b=10,20
    def add(self):
        a, b = 10, 20
        print(a+b)
v1=Variables()
v1.add()
a,b=90,10
class Addition:
    x,y=90,10
    def add(self,m,n):
        print(m+n)
        print(a+b)
        print(self.x+self.y)
add1=Addition()
add1.add(90,10)
a,b=10,20
class Subtraction:
    a,b=10,20
    def sub(self,a,b):
        print(a-b)
        print(self.a-self.b)
        print(globals()['a']-globals()['b'])
s1=Subtraction()
s1.sub(10,20)
#Constructor
class Biodata:
    def __init__(self,name,age,sal,marital_status):
        self.name=name
        self.age=age
        self.sal=sal
        self.marital_status=marital_status
    def display(self):
        print("my name is ",self.name)
        print("my age is ",self.age)
        print('my sal is',self.sal)
        print("my marital_status is",self.marital_status)
bd=Biodata("Tharun",21,23000,"male")
bd.display()'''





