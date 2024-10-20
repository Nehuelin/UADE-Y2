def bin_array(n):
    binario = [0 for _ in range(n)]
    bin_array_rec(binario, 0, n)

def bin_array_rec(binario, e, n):
    if e == n:
        print(binario)
    else:
        for i in range(2):
            binario[e] = i
            bin_array_rec(binario, e + 1, n)

bin_array(4)