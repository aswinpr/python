l=100
n=int(input("enter the limit : "))
count=0
for i in range(1,l):
    if count<n:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")
            count=count+1
