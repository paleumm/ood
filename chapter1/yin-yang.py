inp = int(input('Enter Input : '))
SIZE = 2 * inp + 4

out = []

for i in range(SIZE):
    ls = []
    for j in range(SIZE):
        ls.append(".")
    out.append(ls)

for i in range(SIZE//2):
    for j in range(i+1):
        out[i][SIZE//2 - j-1] = '#'

for i in range(SIZE//2):
    for j in range(SIZE//2,SIZE):
        if (i == 0) or (i == SIZE//2 -1):
            out[i][j] = '+'
        elif j == SIZE-1 or j == SIZE//2:
            out[i][j] = '+'
        else:
            out[i][j] = '#'

for i in range(SIZE//2,SIZE):
    for j in range(SIZE//2):
        if (i == SIZE - 1) or (i == SIZE//2):
            out[i][j] = '#'
        elif j == 0 or j == SIZE//2-1:
            out[i][j] = '#'
        else:
            out[i][j] = '+'

for i in range(SIZE//2):
    for j in range(SIZE//2 - i):
        out[i+SIZE//2][SIZE//2 + j] = '+'

for i in range(SIZE):
    for j in range(SIZE):
        print(out[i][j],end="")
    print()