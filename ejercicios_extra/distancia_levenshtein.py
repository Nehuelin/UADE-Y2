def levenshtein(str1, str2):
    m = len(str1)
    n = len(str2)

    prev_row = [j for j in range(n + 1)]
    curr_row = [0] * (n + 1)
 
    for i in range(1, m + 1):
        curr_row[0] = i
 
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                curr_row[j] = prev_row[j - 1]
            else:
                curr_row[j] = 1 + min(
                    curr_row[j - 1],  # Insertar
                    prev_row[j],      # Remover
                    prev_row[j - 1]    # Remplazar
                )
        prev_row = curr_row.copy()
 
    return curr_row[n]


str1 = "kitten"
str2 = "sitting"
distance = levenshtein(str1, str2)
print("Levenshtein Distance:", distance)