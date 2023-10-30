#Definir una funcion que calcule la longitud de ua tupla o cadena que es recibida por parametro
def cal_long(tupla_cadena):
    longitud=len(tupla_cadena)
    return longitud
tupla_cadena=input('Por favor, ingrese una cadena o tupla...\n \n')
print('***********************************************')
print('La longitud de la cadena que ha escrito es de: ', cal_long(tupla_cadena), 'espacios')