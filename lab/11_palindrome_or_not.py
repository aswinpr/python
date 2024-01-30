num=int(input("enter the number: "))
# str_num=str(num)
# rev_num=str_num[::-1]
# if(rev_num == str_num):
#     print("the number",num,"is palindrome")
# else:
#     print("the number",num,"is not palindrome")

def palindrome(num):
    temp=num
    rev=0
    while(num>0):
        rem=num%10
        rev=rev*10+rem
        num=num//10

    return temp==rev

if(palindrome(num)):
    print(num,"is palindrome")
else:
    print(num,"is not palindrome")
