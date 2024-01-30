students={}
n=int(input("enter the limit : "))
for i in range(n):
    name=input("enter name: ")
    age=int(input("enter age : "))
    grade=input("enter grade : ")
    students[name]=age,grade
print(students)
