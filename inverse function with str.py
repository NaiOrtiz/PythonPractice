#Definir una funcion inversa() que calcule la inversion de una cadena. Por ejemplo, la cadena 'estoy probando' deberida devolver la cadena 'odnaborp yoste'
def inverse_function(frase_usuario):
    cadena_inversa=frase_usuario[::-1]
    return cadena_inversa
txt=input('Por favor ingrese un texto: ')
cadena_inversa=inverse_function(txt)

print('Cadena original: ', txt)
print('Cadena invertida: ', cadena_inversa)