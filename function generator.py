#Definir una funcion generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n
#Por ejemplo_ generar_n_caracteres()(5,'x') deberia devolver 'xxxxx')
def generador_caracteres(n,c):
    n_c=n*c
    return n_c
n=input('Por favor, ingrese un caracter: ')
c=int(input('Por favor, ingrese la cantidad de repeticiones: '))
print('El resultado es: ', generador_caracteres(n,c))