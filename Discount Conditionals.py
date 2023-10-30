'''Imaginemos que en nuestra tienda hay un carnet por puntos y que alguien
debe pagar el precio final de compra. Si tiene menos de 100 puntos
realizaremos un descuento del 10%. Si es mayor a 100 y menor a
150 aplicamos un 12%. Si tiene 150 un 15% y sino, el resto de los
casos de mas de 150 , un 20% ¡ Crea la variable puntos y juega con ella!
'''
precio=int(input('Por favor, ingrese el total a pagar: '))
puntos=int(input('Por favor, ingrese el total de puntos que posee: '))

if puntos<100:
    precio_punto=precio-(precio*0.10)
    print('Por la cantidad de puntos que posee, el precio tendrá un descuento del 10%, por lo que el total a pagar es: ',precio_punto)
elif puntos>100 and puntos<150:
    precio_punto=precio-(precio*0.12)
    print('Por la cantidad de puntos que posee, el precio tendrá un descuento del 12%, por lo que el total a pagar es: ',precio_punto)
elif puntos==150:
    precio_punto=precio-(precio*0.15)
    print('Por la cantidad de puntos que posee, el precio tendrá un descuento del 15%, por lo que el total a pagar es: ',precio_punto)
else:
    precio_punto=precio-(precio*0.20)
    print('Por la cantidad de puntos que posee, el precio tendrá un descuento del 10%, por lo que el total a pagar es: ',precio_punto)


    