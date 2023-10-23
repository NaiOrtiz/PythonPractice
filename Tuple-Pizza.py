ing_veg='pimiento', 'tofu'
ing_n_veg='peperoni', 'jamon', 'salmon'

comida=input('Desea una pizza vegetariana o no vegetariana?')
if comida=='vegetariana':
    print('Los ingredientes de la pizza vegetariana son: \n \n' , '-', capitalize(ing_veg[0]),'\n \n -', capitalize(ing_veg[1]))
    print('Por favor, elija uno de los ingredientes anteriormente mencionados...')
if ingrediente=='pimiento' or ingrediente=='tofu':
    print('Su pizza vegetariana posee tomate, mozzarella y', ingrediente)
elif pizza=='no vegetariana':
    print('Los ingredientes de la pizza no vegetariana son: \n \n', '-', capitalize(ing_n_veg[0]), capitalize(ing_n_veg[1]), capitalize(ing_n_veg[2]))
    print('Por favor elija alguno de los ingredientes anteriormente mencionados....')
    