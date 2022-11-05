l = [e for e in input("Enter Input : ").split()]

def sort(L: list) -> list:
    # print(L)
    if len(L) == 1:
        return L
    s = L[-1]
    for i, data in enumerate(L):
        if s >= data:
            s = L.pop(-1)
            L.insert(i, s)
            break
    
    return L

def median(L: list) -> float:
    median = 0.0
    if len(L) % 2 == 0:
        median = (L[(len(L)//2)-1] + L[(len(L)//2)])/2
    else:
        median = L[(len(L))//2]
    return median

if l[0] == 'EX':
    Ans = "ถ้าเก็บ cache ของ sorted list ไว้ใช้ทุกครั้งที่เพิ่มสมาชิกตัวใหม่เข้าไป ผมคิดว่าใช้ insertion หรือ bubble ก็ไม่น่ามีปัญหา เพราะจะวนลูปเต็มที่ n ครั้งเพื่อ insert ตัวสุดท้ายเข้าไป"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    temp = []
    for i in range(len(l)):
        # print(f'b: {temp+[l[i]]}')
        L = sort(temp+[l[i]])
        temp = L
        print(f'list = {l[0:i+1]} : median = {float(median(L))}')