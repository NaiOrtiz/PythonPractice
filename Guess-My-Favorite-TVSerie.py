print('Adivina mi serie favorita')
print('*'*50)
i=('breaking bad')
print('Ayuditas :D')
print('Contiene la letra:', i[0], '2 veces')
print('Contiene', len(i)-1, 'letras')
print('Termina con la letra', i[11])
print('Es una serie con un titulo de dos palabras')
print('La serie trata de un profesor de quimica, y su ex-estudiante :o')
i_ingresado=input('Adivina cual es? ')

if(i_ingresado==i):
    print('Ganaste!! Felicidades!!')
else:
    print('La serie es', i, 'Perdiste D:')



#indice es el numero de la letra de la variable i[3] en hola es a