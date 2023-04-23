def Nhap():
    L=[]
    x=int(input(""))
    n=int(input(""))
    for i in range (n):
        n=int(input(""))
        L=L+[n]
    return x,n,L
def delete(L,x):
    i=0
    while i<len(L):
        if x==L[i]:
            L=L[:i]+L[i+1:]
        else:
            i=i+1
    return L
def inkq(L):
    print(L)
x,n,L=Nhap()
L=delete(L,x)
inkq(L)