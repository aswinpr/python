def bintodec(bin_num):
    dec_num=0
    for i in bin_num:
        dec_num=dec_num*2+int(i)
    return dec_num

bin_num=input("enter the binary number: ")
print(bintodec(bin_num))