n=int(input())

# for i in range (2,n+1,7):
#     if i+3<=n:
#         print(i,i+3, end=" ")
s1=0
s2=0
for i in range (1,n+1):
    if i<10: s1=s1+i
    if i>=10: s2=i%10+i//10
print(s1+s2)
