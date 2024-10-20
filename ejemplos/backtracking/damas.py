def queen_ok(pos, e):
    for i in range(1, e):
        if (pos[i] == pos[e]) or (abs(pos[i] - pos[e]) == abs(i - e)):
            return False
    return True

def queens(n):
    pos = [0 for _ in range(n)]
    return queens_rec(pos, 0)

def queens_rec(pos, e):
    ok = False
    n = len(pos)
    pos[e] = 0
    while(pos[e] < n and not ok):
        if queen_ok(pos, e):
            if e == n-1:
                ok = True
            else:
                ok = queens_rec(pos, e+1)
        pos[e] += 1
    
    return ok

print(queens(8))

    
