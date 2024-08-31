# El rincón surrealista. 
# El Centro de Investigaciones Espaciales de Fraile Muerto tiene un proyecto secreto sobre antimateria cuántica. 
# La antimateria viene en frascos. 
# Cada frasco p tiene asociado un entero positivo pk. 
# Es importante llevar este número a 1 en la menor cantidad de pasos que sea posible. 
# Para ello, podemos realizar tres operaciones:
# Incrementar el número pk en 1: pk → pk + 1.
# Decrementar el número pk en 1: pk → pk − 1.
# Dividir el número por 2: pk → pk /2. 
# Debido a la energía destructiva liberada cuando se realiza el proceso de division, los controles de seguridad sólo permiten que suceda si el número pk es par.
# Encuentre un proceso para minimizar el número de pasos requerido para llevar un valor pk dado a 1

def minimize_reduction_steps(p: int):
    pasos = []
    while p != 1:
        if p % 2 == 0:
            p //= 2
            pasos.append(f"/1 = {p}")
        elif ((p + 1) // 2) % 2 == 0 and p != 3:
            p += 1
            pasos.append(f"+1 = {p}")
        else:
            p -= 1
            pasos.append(f"-1 = {p}")
    return pasos

p = 7
u = minimize_reduction_steps(p)
for paso in u:
    print(paso)
print(len(u))

    