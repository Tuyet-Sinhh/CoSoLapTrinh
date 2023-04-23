L=[]
n=int(input("n="))
for i in range (1,n+1):
    a=int(input())
    L=L+[a]
demduong=0
demchan=0
s=0
for a in L:
    if a>0: demduong=demduong+1
    if a%2==0: 
        s=s+a
        demchan=demchan+1
if demchan>0:
    tb=s/demchan
else: tb=0
print("SND=",demduong,sep="")
print("TBC=",tb,sep="")