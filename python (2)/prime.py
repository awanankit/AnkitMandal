num=int(input("Please enter a number: "))
flag=True
if num>1:
    for i in range(2,int(num**0.5)+1):
        if num%1==0:
            flag=False
            break
    if flag:
        print("The inputed number is  a Prime number.")
    else:
        print("The inputed number is not an Prime number.")
else:
    print("The inputed number is not a Prime number.")