L=[]
while True:
    a=input("Nhap vao mot tu: ")
    if a=="":
        break
    if a not in L:
       L=L+[a]
for a in L:
    print(a)