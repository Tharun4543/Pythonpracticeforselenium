a,b=10,20
print(a+b)#we can call it as addition
first_name="Nagiri"
last_name="Tharun"
print(first_name +" "+last_name)#we can call it as concantanation of the strings.
# print(10 +"ten")#we will get en error..
print("10"+"10")#valid i.e 1010
#formatting
name="Tharun"
age=20
salary=15000
#print("Name is %s age is %d salary is %d" %(name,age,salary))
print("Name is {2} age is {1} salary is{0} ".format(name,age,salary))
#taking input from user by using input function..
x=int(input("enter x value"))
y=float(input("enter y value"))
z=bool(input("enter either 0 or 1"))
print(x+y+z)