n=int(input())
# i=1
s=0
# while i<=n:
#     x=i
#     while x>0:
#         s=s+x%10
#         x=x//10
#     i=i+1
# print(s)
for i in range (1,n+1):
    k=i
    while k>0:
        a=k%10
        s=s+a
        k=k//10
print(s)