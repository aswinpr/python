string=input("enter the string")
firstchar=string[0]
new=firstchar+string[1:].replace(firstchar,"$")    
print(new)
