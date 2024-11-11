# CAFE Y ESTUDIO 

# a) Debido a que la estudiante tiene un numero limitado de capsulas, cada capsula cuenta con una intensidad distinta y el efecto se reduce con cada ingestion, se deberia organizar la secuencia de capsulas de tal forma que la que mayor intensidad tiene se ingiera primero, y el resto se ordene de forma descendiente. Esto se debe a que, al utilizar las mas potentes primero, se garantiza que se utilize su efecto a mayor escala a que si se empezara con las de menos intensidad o intercalados.
# El algoritmo consistiria en ordenar una lista que contiene la intensidad de las capsulas de cafe de forma descendente (mayor a menor)

# b) Corresponde a un algoritmo greedy

# c) El algoritmo propuesto daria como resultado un efecto de 148

def calcular_intensidad_total(L):
    L.sort(reverse=True)
    efecto = 0
    for i in range(len(L)):
        efecto += L[i] * (1 - i * 0.2) if i < 5 else 0
    return efecto

L = [2, 4, 6, 8, 10, 12]
print(calcular_intensidad_total(L))  

def calcular_intensidad_total2(L):
    L.sort(reverse=True)
    efecto = 0
    for i in range(len(L)):
        efecto += 5 * L[i] * (1 - i * 0.2) if i < 5 else 0
    return efecto

L = [11, 7, 8, 6, 4, 12, 5]
print(calcular_intensidad_total2(L))  