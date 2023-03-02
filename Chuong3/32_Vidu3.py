Tieuthu=float(input("Tieu thu="))
if Tieuthu>=1 and Tieuthu<=100:
    Gia=550*Tieuthu
elif Tieuthu<=150:
    Gia=550*100+750*(Tieuthu-100)
elif Tieuthu<=200:
    Gia=550*100+50*750+(Tieuthu-150)*950
else:
    Gia=550*100+50*750+950*50+1350*(Tieuthu-200)
VAT=Gia*0.1
print("Phai tra=",Gia+VAT,sep="")