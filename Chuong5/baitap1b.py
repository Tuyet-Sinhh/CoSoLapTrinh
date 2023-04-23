L=[]
for i in range(1,11):
    n=int(input(""))
    L=L+[n]
x=int(input("x="))
i=0
while i<len(L):
    if L[i]==x: 
         del(L[i])
    else: i=i+1
print(L)
