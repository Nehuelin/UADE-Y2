def kikimuris(M, F):
    """
    Algoritmo de emparejamiento estable basado en el algoritmo de Gale-Shapley.
    
    :param M: Matríz de preferencias de hombres. M[i][j] indica la j-ésima mujer en la lista de preferencias del hombre i.
    :param F: Matríz de preferencias de mujeres. F[i][j] indica la j-ésima posición en la lista de preferencias de la mujer i para los hombres.
    :return: Lista de pares de emparejamiento (hombre, mujer).
    """
    num_hombres = len(M)
    num_mujeres = len(F)
    
    # Inicializar las estructuras de datos
    mujeres_comprometidas = [None] * num_mujeres
    hombres_libres = list(range(num_hombres))
    propuestas = [0] * num_hombres  # Indica el índice de la siguiente mujer a la que cada hombre propondrá

    # Función para obtener el índice de preferencia de un hombre para una mujer
    def preferencia_hombre(mujer, hombre):
        return F[mujer].index(hombre)

    while hombres_libres:
        hombre = hombres_libres.pop(0)
        mujer_index = propuestas[hombre]
        mujer = M[hombre][mujer_index]
        
        propuestas[hombre] += 1  # El hombre propone a la siguiente mujer en su lista
        
        if mujeres_comprometidas[mujer] is None:
            # La mujer está libre y acepta la propuesta
            mujeres_comprometidas[mujer] = hombre
        else:
            hombre_actual = mujeres_comprometidas[mujer]
            # La mujer ya está comprometida con otro hombre
            if preferencia_hombre(mujer, hombre) < preferencia_hombre(mujer, hombre_actual):
                # La mujer prefiere al nuevo hombre
                mujeres_comprometidas[mujer] = hombre
                hombres_libres.append(hombre_actual)  # El hombre actual queda libre
            else:
                # La mujer prefiere al hombre con el que ya está comprometida
                hombres_libres.append(hombre)  # El nuevo hombre queda libre
    
    # Generar la lista de pares de emparejamiento
    parejas_comprometidas = [(hombre, mujer) for mujer, hombre in enumerate(mujeres_comprometidas)]
    
    return parejas_comprometidas

# Ejemplo de uso
# Matríz de preferencias de los hombres (índices de mujeres en orden de preferencia)
M = [
    [0, 1, 2],  # Hombre 0 prefiere a Mujer 0, luego Mujer 1, luego Mujer 2
    [0, 2, 1],  # Hombre 1 prefiere a Mujer 0, luego Mujer 2, luego Mujer 1
    [1, 0, 2]   # Hombre 2 prefiere a Mujer 1, luego Mujer 0, luego Mujer 2
]

# Matríz de preferencias de las mujeres (índices de hombres en orden de preferencia)
F = [
    [0, 1, 2],  # Mujer 0 prefiere a Hombre 0, luego Hombre 1, luego Hombre 2
    [2, 0, 1],  # Mujer 1 prefiere a Hombre 2, luego Hombre 0, luego Hombre 1
    [1, 2, 0]   # Mujer 2 prefiere a Hombre 1, luego Hombre 2, luego Hombre 0
]

resultado = kikimuris(M, F)
print("Pares comprometidos:", resultado)