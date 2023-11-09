n=int(input("enter the number"))
def fibonacci(n):
	result=0
	if n==0 or n==1:
		return n
	else:
		for i in range(0,n):
			result=(i)+(i+1)
			return result

fibonacci(n)
