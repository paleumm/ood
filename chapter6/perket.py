def solve(arr: list):
    ls = combi(arr)
    min = 1000000000
    for e in ls:
        if len(e) == 0:
            continue
        
        proS = 1
        sumB = 0
        for ee in e:
            proS *= ee[0]
            sumB += ee[1]
        
        sb = abs(proS - sumB)

        if sb < min:
            min = sb

    return min


def combi(arr: list) -> list:
    if len(arr) == 0:
        return [[]]
    
    first = arr[0]
    restofArr = arr[1:]
    combsA = combi(restofArr)
    combsB = []

    for comb in combsA:
        c = [first] + comb
        combsB.append(c)
       
    return combsA + combsB

inp = input('Enter Input : ').split(',')

arr = []
for el in inp:
    el = el.split(' ')
    el = list(map(int, el))
    arr.append(el)

print(solve(arr))
