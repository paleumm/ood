inp = [int(i) for i in input("Enter Input : ").split()]

def insertionSort(L: list, n: int) -> list:
    if n <= 1:
        return
    insertionSort(L, n-1)
    key = L[n-1]
    j = n-2

    while(j >= 0 and L[j] > key):
        L[j+1] = L[j]
        j -= 1
    
    L[j+1] = key
    if len(L[n:]) == 0:
        print(f'insert {key} at index {j+1} : {L[:n]}\nsorted')
    else:
        print(f'insert {key} at index {j+1} : {L[:n]} {L[n:]}')

    return L


if len(inp) == 1:
    print(inp[0])
    exit(0)

print(insertionSort(inp, len(inp)))