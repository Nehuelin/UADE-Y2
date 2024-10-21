# Adapte el problema de la subsecuencia común más larga para encontrar el substring común más largo.

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    M = [[0 for _ in range(n+1)] for _ in range(m+1)]
    max_length = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                M[i][j] = M[i-1][j-1] + 1
                max_length = max(max_length, M[i][j])
            else:
                M[i][j] = 0  
    return max_length

X = "CHAMPPOG"
Y = "RTFEFSPOGCHAMPSFETTSRS"
print(lcs(X, Y))  



