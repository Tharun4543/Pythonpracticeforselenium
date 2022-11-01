# a=10 #global variables
# print(a)
# def display():
#     b=10
#     print(b)
# display()
# print(b) #Invalid because 'b' is a local variable, we cannot access outside of the function..
#update the global variable with in the function
a=10
def show():
    global a
    a=40
    print(a)
show()
print(a)