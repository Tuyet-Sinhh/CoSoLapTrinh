n=int(input(""))
s=0
if n>=1 and n<=10**6:
    for i in range (0,n+1,2):
        s=s+i
    print(s)