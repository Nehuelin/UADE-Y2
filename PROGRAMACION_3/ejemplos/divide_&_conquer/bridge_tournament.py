def fixture(T: list[list[int]], inf: int, sup: int):
    if inf == sup - 1:
        T[inf][1] = sup
        T[sup][1] = inf
    else:
        mid = (inf + sup)//2
        fixture(T, inf, mid)
        fixture(T, mid + 1, sup)
        
def completar_T(T: list[list[int]], first: int, last: int):
    len = (last - first + 1) // 2
    first_adversary = first + len
    second_adversary = first
    first_day = len
    last_day = first_day + len
    for j in range(first_day, last_day):
        T[first][j] = first_adversary
        T[first + len][j] = second_adversary
        first_adversary += 1
        second_adversary += 1
    for i in range(first + 1, last - len):
        for j in range(first_day, last_day):
            if j == first_day:
                T[i][j] = T[i - 1][last_day]
                T[i + len][j] = T[i + len - 1][last_day]
            else:
                T[i][j] = T[i - 1][j - 1]
                T[i + len][j] = T[i + len - 1][j - 1]

n = 32  # número de jugadores, debe ser una potencia de 2
T = [[0 for _ in range(n)] for _ in range(n)]

fixture(T, 0, n - 1)
completar_T(T, 0, n - 1)
print(T)