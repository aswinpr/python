w=[]
limit=int(input("enter the limit"))
largest=None
length=0
for i in range(0,limit):
	word=input("enter the words : ")
	w.append(word)


for i in w:
	if(len(i)>length):
		largest=i
		length=len(i)

print("largest word is: ",largest,"and the length is",len(largest))
		

	

