def bin_array(n):
    binario = [0 for _ in range(n)]
    bin_array_rec(binario, 0, n)
    print()
    bin_array_rec2(binario, 0, n)

def bin_array_rec(binario, e, n):
    for i in range(2):
        binario[e] = i
        if e == len(binario) - 1:
            print(binario)   
        else:
            bin_array_rec(binario, e + 1, n)

def bin_array_rec2(binario, e, n):
    if e == len(binario):
        print(binario)
    else:
        for i in range(2):
            binario[e] = i
            bin_array_rec(binario, e + 1, n)

bin_array(4)