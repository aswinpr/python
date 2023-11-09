print("-----Calculator-----")

def calculator(num1,num2,operation):
	if operation == "+":
		return addition(num1,num2)
	elif operation =="-":
		return subtraction(num1,num2)
	elif operation =="*":
		return multiplication(num1,num2)
	elif operation =="/":
		return division(num1,num2)
	elif operation =="**":
		return power(num1,num2)
	else:
		print("invalid operation")
		
		
		


def addition(num1,num2):
	return num1+num2

def subtraction(num1,num2):
	return num1-num2

def multiplication(num1,num2):
	return num1*num2

def division(num1,num2):
	return(num1/000.........................................num2)

def power(num1,num2):
	return num1**num2

num1=int(input("enter the number 1: "))
num2=int(input("enter the number 2: "))
operation=str(input("select the operator +,-,*,/,** : "))
result=calculator(num1,num2,operation)
print("result is",result)
