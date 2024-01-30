def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def pow(num1,num2):
    return num1**num2
def calculator(num1,num2,operation):
    if operation=="+":
        return add(num1,num2)
    elif operation=="-":
        return sub(num1,num2)
    elif operation=="*":
        return multiply(num1,num2)
    elif operation=="/":
        return div(num1,num2)
    elif operation=="^":
        return pow(num1,num2)
    else:
        print("invalid operation!")
num1=float(input("enter the number 1: "))
operation=input("select operator: +  -  *  /  ^  : ")
num2=float(input("enter number two : "))
result=print(calculator(num1,num2,operation))
    