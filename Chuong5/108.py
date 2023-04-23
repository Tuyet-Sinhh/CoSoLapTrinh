duong=[]
soko=[]
am=[]
while True:
    a=input("")
    if a=="":
        break
    a=int(a)
    if a<0: am.append(a)
    if a==0: soko.append(a)
    if a>0: duong.append(a)
for a in am:
    print(a)
for a in soko: print(a)
for a in duong: print(a)
    