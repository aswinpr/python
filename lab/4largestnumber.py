num_1=int(input("enter number 1 : "))
num_2=int(input("enter number 2 : "))
num_3=int(input("enter number 3 : "))
if (num_1 > num_2 and num_1 > num_3):
    print("largest number is ",num_1)
elif(num_2 > num_1 and num_2 > num_3):
    print("largest number is ",num_2)
else:
    print("largest number is ",num_3)
