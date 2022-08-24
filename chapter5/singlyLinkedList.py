class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return f'{self.data}'

class LinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.length = 0

    def __str__(self) -> str:
        current, s = self.head, []
        while current.next is not None:
            s.append(current.next.data)
            current = current.next
            
        s = '->'.join(s)
        return s

    def __len__(self):
        return self.length

    def isEmpty(self):
        return self.head.next is None

    def append(self, data):
        node = Node(str(data), None)
        cur = self.head
        # print(f'append {cur}')
        while cur.next is not None:
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
        
        while cur.next is not None:
            # print(f'{cur} {cur.next} {idx}')
            if idx == index:
                node.next = cur.next
                cur.next = node
                break
                
            cur = cur.next
            idx += 1
        self.length += 1

class Solver(LinkedList):
    def __init__(self, input:str):
        super().__init__()
        self.initial = input

    def solve(self):
        init = self.initial[0]
        if init == '':
            print(f'List is empty')
        else:
            init = init.split()
            for e in init:
                self.append(e)
            print(f'link list : {self}')
        for i in range(1,len(self.initial)):
            ele = self.initial[i].strip()
            ele = ele.split(':')
            if int(ele[0]) < 0 or int(ele[0]) > len(self):
                print('Data cannot be added')
            else:
                print(f'index = {ele[0]} and data = {ele[1]}')
                self.insert(int(ele[0]), ele[1])
            if self.isEmpty():
                print(f'List is empty')
            else:
                print(f'link list : {self}')

inp = input('Enter Input : ').split(',')

solver = Solver(inp)
solver.solve()

