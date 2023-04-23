L=[]
n=int(input("n="))
while n<4:
    print("Lỗi!!! Phải nhập nhiều hơn 4 giá trị")
    n=int(input("n="))
for i in range(1,n+1):
         a=int(input())
         L=L+[a]
         if n<4:
             break
B=L.copy()
def Xoa():
    B.sort()
    del B[0:2]
    del B[-2:]
    return B
B=Xoa()
print(B)
print(L)