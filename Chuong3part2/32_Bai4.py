for i in range (10):
    a=float(input("a="))
    b=float(input("b="))
    c=input("Toan tu:")
    if c=="+":
        print(a,"+",b,"=",a+b,sep="")  
    if c=="-":
        print(a,"-",b,"=",a-b,sep="")   
    if c=="*":
        print(a,"*",b,"=",a*b,sep="") 
    if c=="/":
        print(a,"/",b,"=",a/b,sep="")
    d=input("Tiep tuc:")
    if d=="T" or d=="t":
        break