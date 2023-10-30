#Definir una funcion es_palindromo() que reconoce palindromos, es decir, palabras que tienen el mismo aspecto
#escritas invertidas), por ejemplo, radar
def inverse_phrase(frase_usuario):
    frase_inversa=frase_usuario[::-1]
    if frase_inversa==frase_usuario:
        print('Su palabra ',frase_usuario, ', es un palindromo!! :D \n \n Al revés seria: ', frase_inversa)
    else:
        print('Su palabra ',frase_usuario, ', no es palindromo :( \n \n Al revés sería: ', frase_inversa)
frase_usuario=input('Por favor, ingrese su palabra: ')
inverse_phrase(frase_usuario)