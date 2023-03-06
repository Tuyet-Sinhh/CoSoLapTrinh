n=int(input("n="))
s=1
for i in range (1,n+1):
    s=s*i
    if n==0:
        print(s=1)
print(n, "!", "=", s, sep=(""))
