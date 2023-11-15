details={}
n=int(input("enter the limit"))
for i in range(n):
	name=input("enter name : ")
	mark=int(input("enter the mark obtained : "))
	details[name]=[mark]
ls=list(details)
ls.sort()
print("sorted in ascending order")
print(ls)
ls.sort(reverse=True)
print("sorted in ascending order")
print(ls)
