class details:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
    def __str__(self):
        print("My name is",self.name)
        print("My gender is",self.gender)
        print(self.age)
d1=details("Tharun","Male",20)
print(d1)
