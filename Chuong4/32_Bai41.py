def nhap():
    n=int(input("n="))
    return n
def giaithua(n):
    s=1
    if n==0:
        return s
    else:
        for i in range (1,n+1):
            s=s*i
    return s
def inkq(n,s):
    print(n,"!=",s,sep="")
n=nhap()
s=giaithua(n)
inkq(n,s)
        