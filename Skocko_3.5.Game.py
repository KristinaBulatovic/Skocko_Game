import random


lista = ["skocko","tref","pik","karo","herc","zvezda"]
lista2 = []
pobeda = "Poraz!"

for i in range(4):
    a = random.choice(lista)
    lista2.append(a)

for i in range(6):
    lista3 = []
    for j in range(4):
        pokusaji = input(">")
        lista3.append(pokusaji)

    if lista2 == lista3:
        pobeda = "Pobeda!!"
        print(pobeda)
        break
    else:
        b = 0
        c = 0
        lista4 = lista2[:]
        lista5 = lista3[:]
        lista6 = []
        for t in range (4):
            if lista2[t] == lista3[t]:
                b += 1
                lista6.append(t)
        print("Na pravom mestu: ", b)
        lista6.sort(reverse = True)
        for i in lista6:
            del lista4[i]
            del lista5[i]
        for l in lista4:
            if l in lista5:
                c += 1
                lista5.remove(l)
        print("Pogresno mesto: ", c)


if pobeda == "Poraz!":
    print("Izgubili ste!!!")
    print("Kombinacija je: ", lista2)
                

        
        
                
                
        
