number1= int(input("enter the first number:"))
number2=int(input("enter the second number:"))
number3=int(input("enter the third number:"))

if number1>number2 and number1>number3:
    print("number1 is largest",number1)
elif number2>number1 and number2>number3:
    print("number 2 is larger",number2)
else:
    print("number3 is larger",number3)
    