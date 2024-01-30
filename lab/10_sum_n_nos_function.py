def sum_of_n_numbers(num):
    sum=0
    for i in range(1,num+1):
        sum=sum+i
    return sum
num=int(input("enter the number: "))
result=sum_of_n_numbers(num)
print("sum of first",num," number is",result)
