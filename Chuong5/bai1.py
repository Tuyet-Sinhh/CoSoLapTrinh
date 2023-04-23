def Nhap():
    L=[]
    x=int(input(""))
    k=int(input(""))
    n=int(input(""))
    for i in range (1,n+1):
        n=int(input(""))
        L=L+[n]
    
    
    return x,k,n,L
def add(L,x,k):
    if k>len(L):
        L=L+[x]
    else:
        L=L[:k]+[x]+L[k:]
    return L
def inkq():
    print(L)
x,k,n,L=Nhap()
L=add(L,x,k)
inkq()