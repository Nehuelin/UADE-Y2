def fibonacci(n):
    fibo = []
    if n <= 1:
        return n
    else:
        for i in range(n+1):
            if i <= 1:
                fibo.append(i)
            else:
                fibo.append(fibo[i-1] + fibo[i-2])
        
        return fibo[n]

print(fibonacci(10))  # 55
# Costo O(n), mejor que el algoritmo recursivo que tiene costo O(2^n)