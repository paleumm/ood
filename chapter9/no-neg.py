inp = [int(i) for i in input("Enter Input : ").split()]

def sort(L: list) -> list:
    for i in range(len(L)):
        if L[i] < 0:
            continue
        for j in range(0, len(L)-i-1):
            # if L[j] < 0:
            #     continue
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
            
    return L

print(*sort(inp))