M1=float(input("M1="))
M2=float(input("M2="))
M3=float(input("M3="))
S=float(input("S="))
if S<=100:
    print("Phai tra=" ,M1*S , seb="") 
elif S<=150:
    Gia=100*M1+(S-100)*M2
    print("Phai tra=", Gia, seb="")   
else:
    Gia=100*M1+50*M2+(S-150)*30
    print("Phai tra=", Gia, sep="")