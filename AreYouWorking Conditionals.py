'''Partiendo de la tarifa anual (que puede cambiar), nos piden que debemos calcular el precio de la tarifa de nuestro polideportivo, sabiendo las siguientes condiciones:
Criterio 1: Si es mayor de edad y esta trabajando -> Paga el 100%
Criterio 2: Si es menor de edad y esta trabajando -> Paga el 95%
Criterio 3: Si es mayor de edad y no esta trabajando -> Paga el 75%
Criterio 4: Si es menor de edad y no esta trabajando -> Paga el 50%
'''
print('Bienvenido!! Por favor, responda las siguientes preguntas...')
edad = int(input('Por favor, ingrese la edad: '))
trabaja = input('¿Está trabajando? (Por favor, solo responda SI o NO): ').strip().lower()
tarifa_anual = float(input('Por favor, ingrese la tarifa anual: '))

if edad >= 18:
    if trabaja == 'si':
        precio = tarifa_anual
    else:
        precio = tarifa_anual * 0.75  
else:
    if trabaja == 'si':
        precio = tarifa_anual * 0.95  
    else:
        precio = tarifa_anual * 0.50 

print('El precio de la tarifa es: $', precio)
