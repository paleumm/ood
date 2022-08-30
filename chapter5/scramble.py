class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return f'{self.data}'

class LinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.length = 0

    def __str__(self) -> str:
        current, s = self.head, []
        while current.next is not self.tail:
            s.append(str(current.next.data))
            current = current.next
        
        s = ' '.join(s)
        return s

    def __len__(self):
        return self.length

    def isEmpty(self):
        return self.head.next is None

    def append(self, data):
        node = Node(str(data), self.tail)
        cur = self.head
        # print(f'append {cur}')
        while cur.next is not self.tail:
            cur = cur.next
        cur.next = node
        # print(f'len = {l}')
        self.length += 1

    def insert(self, index, data):
        if index == self.length:
            self.append(data)
            return

        node = Node(str(data), None)
        idx = 0
        cur = self.head
        # print(cur.next)
        
        while cur.next is not self.tail:
            # print(f'{cur} {cur.next} {idx}')
            if idx == index:
                node.next = cur.next
                cur.next = node
                break
                
            cur = cur.next
            idx += 1
        self.length += 1

def createLL(LL: list) -> LinkedList:
    out = LinkedList()
    for L in LL:
        out.append(L)
    # print(out)
    return out

def printLL(head: LinkedList) -> str:
    return f'{head}'

def SIZE(head: LinkedList) -> int:
    return len(head)

def bottomup(head: LinkedList, b: float ,size: int, de=False) -> LinkedList:
    idx = float(size) * b / 100
    idx = int(idx)

    if de:
        idx = size - idx
    LL = LinkedList()
    
    count = 0
    cur = head.head
    while cur.next is not head.tail:
        if count >= idx:
            LL.append(cur.next.data)

        cur = cur.next
        count += 1
    
    count = 0
    cur = head.head
    while cur.next is not head.tail:
        if count < idx:
            LL.append(cur.next.data)

        cur = cur.next
        count += 1

    return LL

def riffle(head: LinkedList, r: float ,size: int) -> LinkedList:
    idx = float(size) * r / 100
    idx = int(idx)
    LL= LinkedList()
    LL1= LinkedList()
    LL2= LinkedList()

    count = 0
    cur = head.head
    while cur.next is not head.tail:
        if count < idx:
            LL1.append(cur.next.data)
        cur = cur.next
        count += 1
    
    count = 0
    cur = head.head
    while cur.next is not head.tail:
        if count >= idx:
            LL2.append(cur.next.data)
        cur = cur.next
        count += 1

    lenLL1 = len(LL1)
    lenLL2 = len(LL2)
    count1 = count2 = 0
    curLL1, curLL2 = LL1.head, LL2.head
    while count1 < lenLL1 and count2 < lenLL2:
        LL.append(curLL1.next.data)
        count1 += 1
        LL.append(curLL2.next.data)
        count2 += 1
        curLL1 = curLL1.next
        curLL2 = curLL2.next
        
    
    while count1 < lenLL1:
        LL.append(curLL1.next.data)
        curLL1 = curLL1.next
        count1 += 1

    while count2 < lenLL2:
        LL.append(curLL2.next.data)
        curLL2 = curLL2.next
        count2 += 1
    return LL

def deriffle(head: LinkedList, r, size):
    idx = float(size) * r / 100
    idx = int(idx)

    
    LL1= LinkedList()
    LL2= LinkedList()
    LL3= LinkedList()

    
    countLL1 = 0
    countLL2 = 0
    len1 = idx
    len2 = size - idx

    addtailLL1 = False
    if len1 > len2:
        addtailLL1 = True

    count = 0
    cur = head.head
    while cur.next is not head.tail:

        if countLL1 < len1 and countLL2 < len2:
            if count % 2 == 0:
                LL1.append(cur.next.data)
                countLL1 += 1
            elif count % 2 != 0:
                LL2.append(cur.next.data)
                countLL2 += 1
        else:
            if addtailLL1 and countLL2 >= len2:
                LL1.append(cur.next.data)
                countLL1 += 1
            elif not addtailLL1 and countLL1 >= len1:
                LL2.append(cur.next.data)
                countLL2 += 1

        cur = cur.next
        count += 1

    LL = LinkedList()
    cur = LL1.head
    while cur.next is not LL1.tail:
        LL.append(str(cur.next.data))
        cur = cur.next

    cur = LL2.head
    while cur.next is not LL2.tail:
        LL.append(str(cur.next.data))
        cur = cur.next
    return LL

def scarmble(head: LinkedList, b, r, size):
    L1 = bottomup(head, b, size)
    print(f'BottomUp {b:.3f} % : {L1}')
    L2 = riffle(L1, r, size)
    print(f'Riffle {r:.3f} % : {L2}')
    L3 = deriffle(L2, r, size)
    print(f'Deriffle {r:.3f} % : {L3}')
    L4 = bottomup(L3, b, size, de=True)
    print(f'Debottomup {b:.3f} % : {L4}')

    # L2 = bottomup(L1, b, size, de=True)
    # print(f'DebottomUp {b:.3f} % : {L2}')

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)