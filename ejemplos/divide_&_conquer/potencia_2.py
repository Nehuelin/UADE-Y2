def potencia(a: int, n: int) -> int:
    if n == 2:
        return a*a
    else:
        quad = potencia(a, n//2)
        return quad*quad
    
# Version mas eficiente (O(log n))