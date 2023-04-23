import math
def Tinh_canh_huyen(a,b):
    c=math.sqrt(a**2+b**2)
    return c
a=int(input("Nhập cạnh tam giác vuông thứ nhất: "))
b=int(input("Nhập cạnh tam giác vuông thứ hai: "))
c=Tinh_canh_huyen(a,b)
print("Cạnh huyền của tam giác vuông là:",c)