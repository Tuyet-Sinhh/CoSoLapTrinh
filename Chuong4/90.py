def isInteger(n):
    n=n.strip()
    if len(n)<1:
        return False    
    elif n[0] in ["+","-"]:
        n=n[1:]
        if n.isdigit(): #isdigit là hàm ktra xem các kí tự trong chuỗi phải là số ko
            return True
        else: return False
nhap=input("Nhap 1 chuoi: ")
if isInteger(nhap):
    print("Chuoi dai dien cho 1 so nguyen hop le")
else:
    print("Chuoi khong dai dien cho 1 so nguyen hop le")