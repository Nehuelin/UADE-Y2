def binary_search(u: list[int], ini: int, fin: int, x: int) -> None:
    if ini > fin:
        return False
    elif ini == fin:
        return u[ini] == x
    else:
        mid = (ini + fin)/2
        if x == u[mid]:
            return True
        elif x > u[mid]:
            return binary_search(u, mid + 1, fin, x)
        else:
            return binary_search(u, ini, mid - 1, x)