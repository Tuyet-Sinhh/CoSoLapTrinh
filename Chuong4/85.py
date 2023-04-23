def STT(a):
    if a==1: 
        return "first"
    elif a==2: return "second"
    elif a==3: return "third"
    elif a>=4 and a<=12: return (str(a)+"th")
    elif a>12: return ""
for i in range (1,13):
    print(i,STT(i))
        