#Definir una funcion max() que tome como argumento dos numeros y devuelva el mayor de ellos
def max(num_1, num_2):
    if num_1>num_2:
        print('El numero mayor es: ', num_1)
    else:
        print('El numero mayor es: ', num_2)
   
num_1=int(input('Por favor ingrese num_1: '))
num_2=int(input('Por favor ingrese num_2: '))
max(num_1,num_2)