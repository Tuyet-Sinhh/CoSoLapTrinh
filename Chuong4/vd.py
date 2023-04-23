bangchuyenso = {'0': 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'A' : 10 , 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}
def nhap():
    n=input('Nhap so cua ban:')
    return n
def fhemsthem():
    global hemuoi 
    hemuoi=0
    dodai=len(n)-1
    for digit in n:
        hemuoi += bangchuyenso[digit]*16**dodai
        dodai=dodai- 1     
    

def f10t16():
    kq=''
    n=int(n)
    while n>0:
        x=n%16
        if x<10:
            kq = str(x)+kq
        else:
            kq=kq+chr(x+55)
        n = n//16
    return kq
def inkq():
    
    print ("Gia tri cua chuoi thập  phân được chuyển đổi tu thập luc phân là: ", hemuoi)
    print('Gia tri cua chuoi thập luc phân được chuyển đổi tu thập phân là:',kq)

n=nhap()
fhemsthem()
kq=f10t16()
inkq()