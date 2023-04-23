n=int(input(""))
s=0
if n>0 and n<10**6:
    if n<10: print("0")
    else:
        for i in range(1,3):
            s=s+n%10
            n=n//10
        print(s)    