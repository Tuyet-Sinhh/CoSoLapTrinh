n=int(input(""))
dem=0
for i in range(1,n+1):
    if n>=0 and n<=10**6:
        if i%3==0 and i%5==0:
            dem=dem+1
print(dem)