n=int(input("enter the number:"))
def bin(n):
    result=0
    strl=str(n)
    for i in range(0,len(strl)):
        rem=n%10
        result=result+(rem*(2**i))
        n=n//10
    print(result)
bin(n)

