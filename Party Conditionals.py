''' Determinar si alguien es menor de edad o no. Pide al usuario la
edad por pantalla e imprime por pantalla si puede acceder a nuestra
fiesta nocturna de BigBayData.com'''
print('Bienvenidos a BigBayData, para acceder a nuestra fiesta, ingrese su nombre y edad.')
nombre=input('Nombre: ')
edad=int(input('Edad: '))

if edad>=18:
    print('Bienvenido', nombre.capitalize(), 'a BigBayData!!! Para comprar las entradas ingrese aqui')
else:
    print('Lo sentimos', nombre.capitalize(), ', no cumple con la edad requerida para ingresar a nuestro evento :(')
    