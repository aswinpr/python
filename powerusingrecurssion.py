def power(base,exponent):
	if exponent==0:
		return 1
	elif exponent==1:
		return base
	else:
		return base*power(base,exponent-1)
base=int(input("enter the base"))
exponent=int(input("enter the exponent"))
result=power(base,exponent)
print("result is ",result)






































































