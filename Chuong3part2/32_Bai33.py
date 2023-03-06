i=1
while i<10:
    j=1
    while j<10:
        s=i*j
        print(str(s).rjust(3), end=" ")
        j=j+1
    print()
    i=i+1