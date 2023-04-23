def cangiua(chuoi, dorong):
    return " "*dorong + chuoi
chuoi= input("Nhập vào một chuỗi: ")
dorong = int(input("Nhập vào độ rộng của màn hình: "))
chuoicangiua = cangiua(chuoi, dorong)
print(chuoicangiua)