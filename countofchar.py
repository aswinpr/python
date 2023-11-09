string=input("enter the string : ")
count=0
for i in string[::-1]:
	if i != " ":
		count=count+1

print("length of string is: ",count)
