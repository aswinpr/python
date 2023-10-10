n = int(input("Enter the number of prime numbers required : "))
if n >= 1:
    print("\n\nFirst", n, "prime numbers are :  2", end=" ")
count = 2
i = 3
while count <= n:
    c = 2
    while c < i:
        if i % c == 0:
            break
        c += 1
    if c == i:
        print(i, end=" ")
        count += 1
    i += 1
    
