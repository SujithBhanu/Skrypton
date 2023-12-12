num=int(input("Enter the range of Fibnocci number you wana print : "))
a1=0
b1=1
count=0
if(num<0):
    print("Enter valid range")
elif(num==0):
    print(a1)
else:
    while(count<num):
        print(a1,end=",")
        c=a1+b1
        a1=b1
        b1=c
        count+=1