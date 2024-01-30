num1=int(input("enter the number 1: "))
num2=int(input("enter the number 2: "))
operation = input("+,-,*,/,,//,%")

if(operation == "+"):
    result=num1+num2
elif(operation == "-"):
    result= num1-num2
elif(operation == "*"):
    result=num1*num2
elif(operation == "/"):
    result=num1 / num2
elif(operation == "//"):
    result=num1 // num2
elif(operation == "%"):
    result=num1%num2
else:
    print("invalid operation")

print("the result of",num1," ",operation," ",num2,":",result)