a=int(input(""))
b=int(input(""))
n=int(input(""))
if (a>1 and b>1 and n>0) and (a<10**9 and b<10**9 and n<10**9):
    if n==a+b: print("+")
    elif n==a-b: print("-")
    elif n==a*b: print("*")
    elif a/b==n: print("/")
    else:
        print("NO")

