#positional arguments
# def area(a,b):
#     print("the area of square is",a*b)
# area(10,20)
#keyword arguments
# def evennumbers(a,b,c):
#     return a+b+c
# result=evennumbers(c=12,a=13,b=34)
# print(result)
#using positional arguments and keywords arguments
# def display(a,b,c):
#     print(a+b+c)
# display(a=22,34,c=90)   #positional argument follows keyword argument
#default arguments
# def add(a=20,b=30):
#     print(a+b)
# add()
#variable arguments
# def list(*names):
#     for name in names:
#         print(name)
# list("tharun","deepar","devika mam","sandeep")
#keyword variable length arguments
def detailsofperson(**person):
    for i,j in person.items():
        print(i,j)
detailsofperson(name="tharun",age=24)
