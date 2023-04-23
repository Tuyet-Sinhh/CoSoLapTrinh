def Nhap():
    L=[]
    for i in range(1,11):
        n=int(input(""))
        L=L+[n]
    x=int(input("x="))
    return L,x
def Inkq(L):
    for x in L:
        print(x, end=" ")
    print()
def caua(x,L):
    for i in range(len(L)):
        if L[i]==5:
            L[i]=x
    Inkq(L)

        
def caub(x,L):
    i=0
    while i<len(L):
        if L[i]==x: 
            del(L[i])
        else: i=i+1
    Inkq(L)

L,x=Nhap()
caua(x,L)
caub(x,L)


