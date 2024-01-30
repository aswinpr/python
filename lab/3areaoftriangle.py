A = int(input("enter the length 1: "))
B = int(input("enter the length 2 : "))
C = int(input("enter the length 3:"))
s=(A+B+C)/2
area=(s*(s-A)*(s-B)*(s-C))**0.5
print(f"{area:.2f}")