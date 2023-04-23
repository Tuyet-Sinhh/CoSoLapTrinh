def Nhap():
    global a,b,c
    a=float(input("Do dai canh thu nhat a= "))
    b=float(input("Do dai canh thu hai b= "))
    c=float(input("Do dai canh thu ba c= "))
    return a,b,c
def Ktra(a,b,c):
    if a<b+c and b<a+c and c<a+b:
        return True
    else:
        return False
def Inkq():
    if Ktra(a,b,c):
        print("a,b,c co the tao thanh 1 tam giac")
    else: print("a,b,c khong the tao thanh 1 tam giac")
a,b,c=Nhap()
Inkq()