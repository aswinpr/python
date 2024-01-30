def power(base,exponent):
    if exponent==0:
        return 1
    elif exponent==1:
        return base
    else:
        return base*power(base,exponent-1)
base=float(input("enter base : "))
exponent=int(input("enter exponent : "))
result=power(base,exponent)
print(result)