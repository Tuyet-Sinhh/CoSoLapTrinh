a=int(input(""))
b=int(input(""))
s=0
if a==b: print(0)
elif a<=b:
    for i in range (a+1,b+1,1):
        s=s+i
    print(s)