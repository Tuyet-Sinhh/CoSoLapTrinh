LA=[]
n=int(input("n="))
for i in range (1,n+1):
    a=int(input())
    LA=LA+[a]
LA.reverse()
LB=LA.copy()
print(LB)
LB.sort()
print(LB)
