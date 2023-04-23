L=[]
n=int(input("n="))
for i in range (1,n+1):
    a=int(input())
    L=L+[a]
s=0
for i in range(n):
    if i%2!=0:
        s=s+L[i]
print("Tong=",s,sep="")
    