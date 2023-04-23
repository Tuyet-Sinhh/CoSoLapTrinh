L=[]
n=int(input("n="))
for i in range (1,n+1):
    a=int(input())
    L=L+[a]
M=[]
for x in L:
    if x not in M:
        M=M+[x]
for x in M: print(x, end=" ")
        