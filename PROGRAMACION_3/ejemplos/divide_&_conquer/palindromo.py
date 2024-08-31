def palindrome(u: list[int], ini: int, fin: int) -> bool:
    if ini >= fin:
        return True
    elif u[ini] != u[fin]:
        return False
    else:
        return palindrome(u, ini + 1, fin - 1)
    
