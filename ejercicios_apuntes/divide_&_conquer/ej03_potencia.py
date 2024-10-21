# Calcular a^n cuando n es una potencia de 2.

def potencia(a: int, n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        return potencia(a, n // 2) * potencia(a, n // 2)

# Test
a = 2
n = 8
print(potencia(a, n)) # 256