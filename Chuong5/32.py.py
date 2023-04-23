myPets = ['Zophie', 'Pooka', 'Fat-tail']
while True:
    print('Enter a pet name:')
    name = input()
    if name=="":
        break
    if name not in myPets:
        myPets=myPets+[name]
        print(myPets)
    else:   
        print(name + ' đã có.')