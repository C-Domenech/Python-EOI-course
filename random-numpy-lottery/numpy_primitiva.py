import numpy

primitiva = numpy.random.choice(50,7,0)
reintegro = numpy.random.randint(0, 9)
complementario = primitiva[-1]

primitiva = numpy.delete(primitiva,-1)

primitiva.sort()

print("Número ganadores: ",primitiva,"\nComplementario: ",complementario,"\nReintegro: ",reintegro)