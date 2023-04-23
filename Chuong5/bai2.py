def Nhap():
    L=[]
    x=int(input(""))
    n=int(input(""))
    for i in range (n):
        n=int(input(""))
        L=L+[n]
    
    
    return x,n,L
def search(L,x):
    for i in range(len(L)):
        if x==L[i]: 
            return i
    return None
def inkq(L,x):
    print(search(L,x))
x,n,L=Nhap()
search(L,x)
inkq(L,x)
