input_list = input('Enter Your List : ').split()
input_list= list(map(int, input_list))

def sumArr(arr):
    out = []
    count = 0
    if len(arr) < 3:
        print('Array Input Length Must More Than 2')
        return
    
    for i in arr:
        for j in arr:
            for k in arr:
                if i==j and i==k and j==k and i==0:
                    out.append([0,0,0])
                if i + j + k == 0 and i != j and i != k and j!= k:
                    out.append(sorted([i,j,k]))

    out = set(tuple(x) for x in out)
    out = sorted(list(list(x) for x in out))
    print(out)

sumArr(input_list)
