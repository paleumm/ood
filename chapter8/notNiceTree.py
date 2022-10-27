inp = input('Enter Input : ').split('/')
nd = [int(i) for i in inp[1].split()]
n = int(inp[0])

if len(nd) != n//2 + 1:
    print("Incorrect Input")
    exit(0)

# node เริ่มตั้งแต่ 1-n เลยต้องมี n+1 ตัว 
L = [None]*(n+1)

# ใส่ input เข้าไปใน L ตามตำแหน่วใน tree
for i in range(n//2+1, n+1):
    L[i] = nd[i-(n//2+1)]

for i in range(n,0,-1):
    if L[i] is None:
        # หา min จาก node ลูกทั้ง 2 ตัว
        m = min(L[2*i], L[2*i+1])
        L[2*i] -= m
        L[2*i+1] -= m
        L[i] = m

x = 0
for i in range(1, n+1):
    x += L[i]

print(x)