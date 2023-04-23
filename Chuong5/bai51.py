
def Input():
    L=[]
    n=int(input("n="))
    for i in range (1,n+1):
        a=int(input())
        L=L+[a]
    x=int(input("x="))
    return L,x
def FirstAndLast(L):
    k=[L[0],L[-1]]
    print(k)
    return k
def Search(L,x):
    if x in L:
        return True
    return False
L,x=Input()
k=FirstAndLast(L)
t=Search(L,x)
print(t)
        