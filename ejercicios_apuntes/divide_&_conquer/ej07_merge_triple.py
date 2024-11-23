# Dado un Vector A  de números enteros, ordenarlo en forma creciente. Utilizar el 
# método de ordenamiento Merge-Sort, pero dividiendo el vector en 3 subvectores y 
# analizar el costo. 

def merge_sort_three(A):
    if len(A) <= 1:
        return A
    
    one_third = len(A) // 3
    two_third = 2 * len(A) // 3
    left = A[:one_third]
    middle = A[one_third:two_third]
    right = A[two_third:]
    
    left = merge_sort_three(left)
    middle = merge_sort_three(middle)
    right = merge_sort_three(right)

    return merge_three(left, middle, right)

def merge_three(left, middle, right):
    result = []
    i = j = k = 0

    while i < len(left) or j < len(middle) or k < len(right):
        smallest = float('inf')
        if i < len(left):
            smallest = min(smallest, left[i])
        if j < len(middle):
            smallest = min(smallest, middle[j])
        if k < len(right):
            smallest = min(smallest, right[k])
        if i < len(left) and smallest == left[i]:
            result.append(left[i])
            i += 1
        elif j < len(middle) and smallest == middle[j]:
            result.append(middle[j])
            j += 1
        elif k < len(right) and smallest == right[k]:
            result.append(right[k])
            k += 1
    
    return result


A = [34, -23, 7, 0, -15, 18, 12, -9, 3, -4, 25]
print("Original:", A)
sorted_A = merge_sort_three(A)
print("Ordenado:", sorted_A)