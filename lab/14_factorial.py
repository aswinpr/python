def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        result=factorial(n-1)
        return n*result
n=int(input("enter the number: "))
print("factorial of",n,"is :",factorial(n))