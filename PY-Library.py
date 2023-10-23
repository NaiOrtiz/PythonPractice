#Funciones de la libreria de PY
#Retorna el valor absoluto del parametro. ABS
a=-23
print('El valor absoluto es: ' ,abs(a))

#Obtiene la conversion a binario. BIN
b=8
print('El valor en binario es: ',bin(b))

#Retorna el caracter en formato de string al valor Unicode. Se basa en la tabla ASTIL. CHR
c=45
print('El valor unicode es: ', chr(c))

#Retorna el cociente y el resto de la divison. DIVMOD
d,e=14,4
f,g=divmod(d,e)
print('El cociente de la division es: ', d, 'y el resto es:', g)

#Convierte la cadena de texto a un numero con coma flotante. FLOAT
h='24.5'
print(float(h))

#Obtiene la conversion hexadecimal. HEX
i=124
print('El valor hexadecimal es:',hex(i))

#Obtiene una cadena de caracteres desde la entrada. INPUT.
j=input('Ingrese algo:')
print(j)

#Convierte la cadena de texto a un numero entero. INT
k='123'
print(int(k))

#Retorna la longitud del objeto tomado como parametro. LEN
l=12,14,16
print(len(l))

#Retorna el mayor de los parametros tomados. MAX
m,n=12,15
mayor=max(m,n)
print(mayor)

#Retorna el menor de los parametros tomados. MIN
o,p=9,4
menor=min(o,p)
print(menor)

#Obtiene la conversion en octal. OCT
q=12
print('La conversion en octal es:',oct(q))

#Retorna el entero unicode que representa. ORD
r='A'
print(ord(r))

#Retorna el valor de x elevado a y. POW
x,y=3,2
potencia=pow(x,y)
print('El resultado de la potencia es:',potencia)

#Retorna el numero flotante pero redondeado a tantos digitos quiera. ROUND (despues de la coma va la cantidad de digitos que queremos)
z=4.31234
print(round(z,2))

#Retorna una version en forma de cadena de texto. STR
u=2,4,1
print(str(u))