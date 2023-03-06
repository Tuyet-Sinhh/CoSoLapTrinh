while True:
    n=int(input(""))
    if n<0:
        break
    s=1
    i=1
    while i<=n:
        s=s*i
        i=i+1
    print(s)