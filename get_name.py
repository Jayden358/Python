#Jayden Williams
#9/19
#get user name

def get_name():
    while True:
        name = input("What is your name")
        if " " in name:
            name = name.replace(" ","QZRX")
        if name.isalpha():
            name = name.replace("QZRX"," ")
            name = name.title()
            return name
        else:
            print("invalid")

def math_fun(x,y):
    if x.isdigit() and y.isdigit()and len(x) <= 2 and len(y) <= 3 :
        x=int(x)
        y=int(y)
    else:
        print("invalid")
        return "you suck at math"
    num1 = x
    num2 = y
    total = num1*num2
    return total
x=int(input("enter a number"))
y=int(input("enter a number"))
if x.isdigit():
    x=int(x)
if y.isdigit():
    y=int(y)    
result = math_fun(x,y)
print(result)
result2 = math_fun(xx,yy)
