from heap_priority_queue import ColaPrioridad

def huffman(texto):
    frecuencia = {}
    for caracter in texto:
        if caracter not in frecuencia:
            frecuencia[caracter] = 0
        frecuencia[caracter] += 1

    cola = ColaPrioridad()
    for caracter, f in frecuencia.items():
        cola.acolar_prioridad(caracter, f)

    while len(cola.cola) > 1:
        f1 = cola.prioridad()
        c1 = cola.primero()
        cola.desacolar()
        f2 = cola.prioridad()
        c2 = cola.primero()
        cola.desacolar()
        cola.acolar_prioridad((c1, c2), f1 + f2)

    arbol = cola.primero()
    codigos = {}
    def dfs(nodo, codigo):
        if isinstance(nodo, tuple):
            dfs(nodo[0], codigo + '0')
            dfs(nodo[1], codigo + '1')
        else:
            codigos[nodo] = codigo
    dfs(arbol, '')

    texto_codificado = ''.join(codigos[caracter] for caracter in texto)

    return texto_codificado, codigos

def decodificar(texto_codificado, codigos):
    texto = ''
    codigo = ''
    for bit in texto_codificado:
        codigo += bit
        if codigo in codigos.values():
            caracter = [k for k, v in codigos.items() if v == codigo][0]
            texto += caracter
            codigo = ''
    return texto

# Ejemplo
texto = 'abracadabra'
texto_codificado, codigos = huffman(texto)
print('Texto codificado:', texto_codificado)
print('Codigos:', codigos)
texto_decodificado = decodificar(texto_codificado, codigos)
print('Texto decodificado:', texto_decodificado)
