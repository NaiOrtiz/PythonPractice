#escribir una funcion que calcule eltotal de una factura tras aplicarle el iva. la cunfioon deberecibir la cantidad sin iva
#y el porcentaje de iva a plicar, ydevolver el total de la factura. Si se invoca la funcio sin pasarle el porcentaje del iva
#debera aplicar un 21%
cant_total=int(input('Por favor, ingrese su factura: '))
porc_iva=int(input('Ahora, ingrese el porcentaje del IVA: '))
             
def iva(cant_total, porc_iva=21):
    iva=(cant_total*21)/100
    total=cant_total+iva
    return(total)


print('Su importe con el 21% del IVA es: ', iva(cant_total,porc_iva))

