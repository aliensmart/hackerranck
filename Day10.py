def binary(n):
    myBin =  bin(n).replace("0b", '')
    print(myBin)
    num = 0
    max_num = 0
    for i in myBin:
        if i=="1":
            num += 1
            if num > max_num:
                max_num = num
        else:
            num = 0

        
    
    print(max_num)

binary(6)