def factorial(n):
	fact=1
	if n==0 or n==1:
		return 1
	else:
		for i in range(1,n+1):
			fact=fact*i
		return fact
n=int(input("enter the number"))
print("factorial is ",factorial(n))
