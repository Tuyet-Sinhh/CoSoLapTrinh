def Nhap():
    L=[]
    x=int(input(""))
    y=int(input(""))
    n=int(input(""))
    for i in range (n):
        n=int(input(""))
        L=L+[n]
    
    return y,x,n,L
def replace(x,L,y):
    for i in range(len(L)):
        if x==L[i]:
            L[i]=y
    print(L)
y,x,n,L=Nhap()
replace(x,L,y)