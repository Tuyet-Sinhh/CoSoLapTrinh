while True:
    n=int(input())
    if n==0: 
        break
    i=1
    a=0
    b=0
    while i<=n:
        if n>0: a=a+1
        else: b=b+1
    i=i+1
    print(a, "so duong")
    print(b,"so am")