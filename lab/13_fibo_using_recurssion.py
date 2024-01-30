def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("enter th enumber: "))
for i in range(1,n+1):
    print(fibonacci(i),end=",")