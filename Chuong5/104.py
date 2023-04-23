L=[]
while True:
    n=int(input())
    L=L+[n]
    if n==0: 
        break
L.sort()
for x in L: 
    if x!=0:
        print(x)
