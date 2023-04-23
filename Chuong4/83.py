def Soluonghang(n):
    for i in range(n):
        a=0
        if i==1: a=10.95
        else: a=2.95*i+10.95
    return a
n=int(input("Nhập vào số lượng hàng: "))
a=Soluonghang(n)
print("Phí vận chuyển là",a)
