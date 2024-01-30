list=[]
num=int(input("enter the limit: "))
for i in range(num):
    name=input("enter name : ")
    list.append(name)
list.sort()
print(list)