def potencia(a: int, n: int) -> int:
    if n == 2:
        return a*a
    else:
        return potencia(a, n//2)*potencia(a, n//2)
    
# Costo O(n)