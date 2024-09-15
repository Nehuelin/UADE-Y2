def encontrar_pico(arr, ini, fin):
    if ini == fin:
        return ini
    
    mid = (ini + fin /2)

    if (arr[mid] >= arr[mid - 1]) and (arr[mid] >= arr[mid + 1]):
        return mid
    
    elif mid > 0 and arr[mid - 1] > arr[mid]:
        return encontrar_pico(arr, ini, mid - 1)
    
    else: 
        return encontrar_pico(arr, mid + 1, fin)