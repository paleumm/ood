def search(x, arr):
    temp = 1_000_001
    for idx, k in enumerate(arr):
        if k > x:
            if temp >= k:
                temp = k
    return temp


inp = input("Enter Input : ").split('/')

arr1 = [int(x) for x in inp[0].split()]
arr2 = [int(x) for x in inp[1].split()]

for x in arr2:
    re = search(x, arr1)
    if re == 1_000_001:
        print('No First Greater Value')
    else:
        print(re)