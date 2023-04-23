# L = 3*[ [x,x-1,x,x-1] for x in range(1,2,1) ]
# L=[(1,0,1,0) for x in range (1,4)]
# print(L)
def is_perfect_number(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

for i in range(1, 10001):
    if is_perfect_number(i):
        print(i)
