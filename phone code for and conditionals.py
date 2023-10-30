''' Tenemos la pantalla del celular bloqueada. Partiendo de un pin secreto, intentaremos desbloquear la pantalla. Tenemos hasta tres intentos.
Simula el proceso con Python. En caso de acceder, lanza al usuario <Login Correcto> , sino <Llamando a la policia>'''
pin_s='milanesasconpure'

for i in range (3):
    pin=(input('Ingrese su PIN: '))
    if pin==pin_s:
        print('LOGIN CORRECTO. BIENVENIDO!!')
        break
    else:
        print('LOGIN INCORRECTO. INTENTELO DE NUEVO...')
        
print('*****************************')
print('Ha agotado todos los intentos. ACCESO DENEGADO. LLAMANDO A LA POLICIA...')
    