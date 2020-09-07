# only first time
'''
fichero = open("guardian.txt", "x")

fichero.write("Pero lo que mas me gustaba de aquel museo era que todo estaba siempre en el mismo sitio. No cambiaba nada. Podias ir cien mil veces distintas y el esquimal seguia pescando, y los pajaros seguian volando hacia el sur, y los ciervos seguian bebiendo en las charcas con esas patas tan finas y tan bonitas que tenian, y la india del pecho al aire seguia tejiendo su manta.")
'''

fichero = open("guardian.txt", "r")
texto = fichero.read()
fichero.close()

i = 1
guardian = {}

for _ in range(texto.count("seguia")):
    start = texto.find("seguia")
    texto = texto[start:]
    coma = texto.find(",")
    punto = texto.find(".")
    end = coma if coma < punto else punto
    frase = texto[:end]
    clave = 'frase ' + str(i)
    guardian.update({clave: frase})
    texto = texto[end+1:]
    i += 1

print(guardian)

# nuevofichero = open("seguia.txt", "x")
nuevofichero = open("seguia.txt", "w")
for x in guardian:
    nuevofichero.write(guardian[x] + '\n')
    print(guardian[x] + '\n')

nuevofichero.close()
