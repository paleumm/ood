def binary(idx: int, arr: list, n: int) -> list:

    if idx == n:
        print("".join(arr))
        return

    arr[idx] = '0'
    binary(idx + 1, arr, n)
    arr[idx] = '1'
    binary(idx + 1, arr, n)

def solve(n : int):
    if n < 0:
        print('Only Positive & Zero Number ! ! !')
        return
    arr = ['0']*n
    if n == 0:
        arr = ['0']
    binary(0,arr,n)

    
    

ip = int(input('Enter Number : '))

# solve(ip)
solve(ip)