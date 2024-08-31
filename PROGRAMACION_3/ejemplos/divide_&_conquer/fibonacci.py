def fib(n: int) -> int:
    if (n <= 1):
        return n
    else:
        return fib(n - 1)+fib(n - 2)

# Costo O(2^n), hay un metodo mas eficiente con programacion dinamica