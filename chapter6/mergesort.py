def mergesort(L : list):
    if len(L) > 1: # not base case
        mid = len(L) // 2
        
        LL = L[:mid]
        RL = L[mid:]

        mergesort(LL)
        mergesort(RL)


        i = 0
        j = 0
        k = 0

        while i < len(LL) and j < len(RL):
            if LL[i] > RL[j]:
                L[k] = LL[i]
                i += 1
            else:
                L[k] = RL[j]
                j += 1

            k += 1

        while i < len(LL):
            L[k] = LL[i]
            i += 1
            k += 1

        while j < len(RL):
            L[k] = RL[j]
            j += 1
            k += 1

    return L


L = input('Enter your List : ').split(',')
L =list(map(int, L))

L = mergesort(L)
print(f'List after Sorted : {L}')