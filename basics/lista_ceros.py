lista = [0, 0, 1, 0, 3, 12]
#lista = [1,3,12,0,0]
#lista = [0,1,0,3,12]
print("Lista original:", lista)
n_ceros = lista.count(0)

for i in range(n_ceros):
    lista.remove(0)
    lista.append(0)

    print("Vuelta", i + 1, ":", lista)
print("Lista final:", lista)
