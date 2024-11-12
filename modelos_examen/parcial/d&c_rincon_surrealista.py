# EL RINCON SURREALISTA

# a) ESTRATEGIA: Se podria dividir el conjunto de numeros en dos subconjuntos en cada recursion, y le preguntamos al brujo si esta en uno de los subconjuntos. Si la respuesta es no, debe estar en el otro. El caso base es cuando queda un solo numero, siendo este el numero ganador.  Si no se cumple el caso base, se agarrar el subconjunto donde podria estar el numero ganador, y continuar la recursion.
# b) Corresponde a la tecnica Divide & Conquer ya que se resuelve un problema mediante la resolucion de subproblemas mas pequeños que llevan a solucionar el problema global
# c) Debido a que el costo del algoritmo es Olog(n), siendo n = 65536 la cantidad de numero, la cantidad de consultas totales es C = log2(n) = 16. Como cada consulta sale $5000, entonces el total es T = C x 5000 = 80000. Como el ultimo ticket no esta incluido en la cuenta, T = 80100. Finalmente podemos concluir que el monto final de ganancia es G = 200000 - T = $119900 
import random

def adivinar_numero(L, x, ini, fin):
    if ini == fin:
        return ini
    medio = (ini + fin) // 2
    if x <= L[medio]:
        return adivinar_numero(L, x, ini, medio)
    else:
        return adivinar_numero(L, x, medio + 1, fin)

L = [i for i in range(1, 65537)]
x = random.randint(1, 65536)
print(adivinar_numero(L, x, 0, len(L)))
