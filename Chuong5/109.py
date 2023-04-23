def Uoc(n):
    L=[]
    for i in range(1,n):
        if n%i==0:
            L.append(i)
    return L
n=int(input("n="))
L=Uoc(n)
print(L)