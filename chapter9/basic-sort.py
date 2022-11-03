inp = [int(i) for i in input("Enter Input : ").split()]

temp = inp[0]
isSort = True

for i in inp:
    if i < temp:
        isSort = False
        break

if isSort:
    print("Yes")
else: 
    print("No")