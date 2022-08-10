def odd_list(al):
    odd = []
    for a in al:
        if a % 2 == 1:
            odd.append(a)
    return odd


print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)