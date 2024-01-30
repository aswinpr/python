string=input("enter a word")
first_letter=string[0]
last_letter=string[-1]
new_string=last_letter+string[1:-1]+first_letter
print(new_string)