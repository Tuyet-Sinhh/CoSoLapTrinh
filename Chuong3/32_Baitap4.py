Toan=float(input())
Ly=float(input())
Hoa=float(input())
DTB=float(Toan*2+Ly*3+Hoa)/6
if DTB<3:
    print("Kem")
elif DTB<5:
    print("Yeu")
elif DTB<6:
    print("Trung binh")
elif DTB<7:
    print("Trung binh Kha")
elif DTB<8:
    print("Kha")
elif DTB<9:
    print("Gioi")
elif DTB<10:
    print("Xuat sac")
