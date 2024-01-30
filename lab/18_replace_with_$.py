string=input("enter a word : ")
fchar=string[0]
newstr=fchar + string[1:].replace(fchar,'$')
print(newstr)