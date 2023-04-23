print('Enter the numbers:')

L = []

while True:
    n = input()
    if n == "":
        break
    L.append(int(n))

n = len(L)
s = sum(L)
tb = s / n

duoi = []
tren = []
for x in L:
    if x > tb:
        duoi.append(x)
    elif x < tb:
        tren.append(x)

print("Below average:", duoi)
print("Average:", tb)
print("Above average:", tren)
