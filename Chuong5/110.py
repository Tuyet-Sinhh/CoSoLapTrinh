def Sohoanhao(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    if s==n:
        return True
    else:
        return False
n=int(input('n='))
print(Sohoanhao(n))
for i in range(1,10001):   
     if Sohoanhao(i):
       print(i)

       
    
        