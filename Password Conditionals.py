'''Guardar una contraseña como password. Crea un sistema de seguridad
donde el ordenador muestre un mensaje <Ordenar Bloqueado. contraseña
incorrecta> si el usuario falla la contraseña. En caso contrario ,
que muestre por pantalla <Bienvenid@>'''
nombre=input('Ingrese su nombre: ')
contraseña=(input('Cree una contraseña: '))
contraseña_1=(input('Bienvenido/a! Por favor, ingrese su contraseña: '))
if contraseña==contraseña_1:
    print('Bienvenido/a ',nombre.capitalize(), ':)')
else:
    print('***CONTRASEÑA INCORRECTA. ORDENADOR BLOQUEADO.***')
