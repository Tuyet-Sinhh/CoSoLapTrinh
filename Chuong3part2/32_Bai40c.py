"""n=int(input("n="))
i=1
while i<=n:
    print(i,end=" ")
    i=i+1
"""
n = 5
for i in range(n):
  s = ""
  for j in range(1,n+1):
    s += str(j) + " "
  print(s)
    