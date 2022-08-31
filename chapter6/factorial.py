def factorial(n: int):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n-1)

n = int(input("Enter Number : "))
print(f'{n}! = {factorial(n)}')