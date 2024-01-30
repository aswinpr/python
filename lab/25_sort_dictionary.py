student={}
n=int(input("enter the limit : "))
for i in range(n):
    name=input("enter name : ")
    age=int(input("enter age : "))
    grade=input("enter grade : ")
    student[name]=age,grade
l=list(student.items())
l.sort()
print("ascending",l)
l.sort(reverse=True)
print("descending",l)
