# Dado un vector de n números naturales ordenados crecientemente, determinar si un número x dado pertenece al vector

def pertenece(v: list[int], x: int, ini: int, fin: int) -> bool:
    if len(v) == 1:
        return v[0] == x
    
    mid = (ini + fin) // 2

    if v[mid] == x:
        return True
    elif v[mid] < x:
        return pertenece(v, x, mid + 1, fin)
    else:
        return pertenece(v, x, ini, mid)

# Test
v = [1, 2, 3, 4, 5]
x = 3
print(pertenece(v, x, 0, len(v) - 1)) # True
        
    
