def raiz_cuadrada_entera(n, low, high):
    if low > high:
        return high  # El punto de mayor valor cuyo cuadrado es menor o igual a n
    
    mid = (low + high) // 2
    mid_cuadrado = mid * mid

    if mid_cuadrado == n:
        return mid
    elif mid_cuadrado < n:
        return raiz_cuadrada_entera(n, mid + 1, high)
    else:
        return raiz_cuadrada_entera(n, low, mid - 1)