#Definir una funcion maxdetres() que tome tres numeros como argumento y devuelva el mayor de ellos
def mayor_3(num_1, num_2, num_3):
    mayor = max(num_1, num_2, num_3)
    return mayor
num_1 = int(input('Ingrese num_1: '))
num_2 = int(input('Ingrese num_2: '))
num_3 = int(input('Ingrese num_3: '))
print('El número mayor entre los 3 es:', mayor_3(num_1, num_2, num_3))
