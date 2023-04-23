def nhap():
    n=int(input("n="))
    return n
def inkq(n):
    for i in range (2,n+1,2):
        print(i, end=" ")
n=nhap()
inkq(n)
print()
t=str(input("Tiep tuc khong?"))
while True:
    n=nhap()
    inkq(n)
    t=str(input("Tiep tuc khong?"))
    if t=="k" or t=="K":
        break
    
    
     