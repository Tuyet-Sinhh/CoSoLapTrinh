LA=[]
n=10
for i in range (10):
    a=int(input())
    LA=LA+[a]
B=LA.copy()
for i in range (0,n-1,2):
    B[i]=LA[i+1]
    B[i+1]=LA[i]
for a in B:
    print(a, end=" ")

