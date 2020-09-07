def feed(pet):
    if not pet['hungry']:
        print(f">>> {pet['name']} está bien alimentado.")
    else:
        pet['hungry'] = False
        pet['weight'] *= 1.5
        print(f">>> {pet['name']} pesa {round(pet['weight'], 2)} y no tiene hambre.")


def play(pet):
    pet['mood'] = 'happy'
    pet['hungry'] = True
    pet['weight'] -= 0.1
    print(f">>> {pet['name']} ha jugado y está feliz.")
    if pet['weight'] <= 0.2:
        print(f">>> {pet['name']} está cansado y hambriento.")


print("¡Bienvenido a la mascota virtual!")
print("Vamos a crear a tu mascota.")
pet = {}
pet['name'] = input("> ¿Cuál es el nombre de tu mascota? ")
pet['age'] = int(input(f"> ¿Cuántos años tiene {pet['name']}? "))
pet['weight'] = float(input(f"> ¿Cuánto pesa {pet['name']}? "))
pet['hungry'] = True
pet['mood'] = 'sad'
pet['photo'] = '<:3 )---'
print(f">>> {pet['name']} tiene {pet['age']} años y pesa {pet['weight']}kg.")
print(f"Ahora podrás cuidar a {pet['name']}.")
print("------------------------------------------------------------------")
answer = input("Escribe 'salir' si quieres dejar de jugar. Pulsa Enter para continuar.")
print("------------------------------------------------------------------")
while answer != 'salir':
    if pet['hungry']:
        print(f">>> {pet['name']} tiene hambre.")
    else:
        print(f">>> {pet['name']} no tiene hambre")

    answer_feed = input(f"> ¿Quieres alimentar a {pet['name']}? Contesta si o no. ")
    if answer_feed.lower() == 'si':
        feed(pet)

    if pet['mood'] == 'sad':
        print(f">>> {pet['name']} está triste.")
    else:
        print(f">>> {pet['name']} está feliz.")
    answer_play = input(f"> ¿Quieres que {pet['name']} juegue? Contesta si o no. ")
    if answer_play.lower() == 'si':
        play(pet)
        if pet['weight'] <= 0.1:
            print(f">>> {pet['name']} ha muerto de inanición.")
            break

    print("------------------------------------------------------------------")
    answer = input("Escribe 'salir' si quieres dejar de jugar. Pulsa enter para continuar.")
    print("------------------------------------------------------------------")
