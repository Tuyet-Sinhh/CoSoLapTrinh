def LaSoNguyenTo(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
def SoHopLe(x):
    if x <= 1:
        return True
    else:
        return False
def NhapVaDem():
    dem = 0
    print("Nhap day so:")
    while True:
        x = int(input(""))
        if SoHopLe(x):
            break
        if LaSoNguyenTo(x):
            dem=dem+1
    return dem
def InKQ(kq):
    print("Co", kq,"so nguyen to")
kq=NhapVaDem()
InKQ(kq)


