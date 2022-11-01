print("This is Exception handling demo")
try:
    string="Tharun"
    print(string[8])


except:
    print("Index out of bound error")
else:
    print("everything is fine")
finally:
    print("Program is completed")
try:
    print(string[4])
except:
    print("Hello")