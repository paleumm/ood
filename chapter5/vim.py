class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = Node('Empty', None, None)
        self.tail = Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def __str__(self):
        cur, s = self.head, []
        while cur.next is not self.tail:
            s.append(str(cur.next.value))
            cur = cur.next
        s = " ".join(s)
        s += " "
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, []
        while cur.prev is not self.head:
            s.append(str(cur.prev.value))
            cur = cur.prev
        s = " ".join(s)
        return s

    def isEmpty(self):
        return self.length == 0

    def append(self, item):
        cur = self.head
        # print(f'append {cur}')
        while cur.next is not self.tail:
            cur = cur.next
        node = Node(item, cur, self.tail)
        self.tail.prev = node
        cur.next = node
        # print(f'len = {l}')
        self.length += 1

    def addHead(self, item):
        cur = self.head.next
        node = Node(item, self.head, cur)
        cur.prev = node
        self.head.next = node
        self.length += 1

    def insert(self, pos, item):
        if pos > self.length - 1:
            self.append(item)
            return
        elif pos < 0:
            idx = -pos
            i = 0
            if idx > self.length - 1:
                self.addHead(item)
                return
            else:
                cur = self.tail
                while cur.prev is not self.head:
                    if i == idx:
                        node = Node(item, cur.prev, cur)
                        cur.prev.next = node
                        cur.prev = node
                    cur = cur.prev
                    i += 1
        else:
            if pos == 0:
                self.addHead(item)
                return
            else:
                cur = self.head
                i = 0
                while cur.next is not self.tail:
                    if i == pos:
                        node = Node(item, cur.prev, cur)
                        cur.prev = node
                        cur.prev.next = node
                    cur = cur.next
                    i += 1
        
        self.length += 1

    def search(self, item):
        cur = self.head
        while cur.next is not self.tail:
            if str(cur.next.value) == str(item):
                return f'Found'
            cur = cur.next
        return f'Not Found'

    def index(self, item):
        cur = self.head
        idx = 0
        while cur.next is not self.tail:
            if cur.next.value == item:
                return idx
            cur = cur.next
            idx += 1
        return -1

    def __len__(self):
        return self.length

    def pop(self, pos):
        if pos > self.length - 1 or pos < -self.length:
            return 'Out of Range'
        elif pos < 0:
            idx = -pos - 1
            i = 0
            
            cur = self.tail
            while cur.prev is not self.head:
                if i == idx:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                cur = cur.prev
                i += 1
        else:
            if pos == 0:
                cur = self.head.next
                cur.next.prev = self.head
                self.head.next = cur.next
            else:
                cur = self.head
                i = 0
                while cur.next is not self.tail:
                    if i == pos:
                        cur.prev.next = cur.next
                        cur.next.prev = cur.prev
                    cur = cur.next
                    i += 1
        
        self.length -= 1
        return 'Success'



class Vim(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        self.cursor = Node('|', self.head, self.tail)
        self.head.next = self.cursor
        self.tail.prev = self.cursor

    def do(self, command: str):
        commands = command.split(',')
        for comm in commands:
            comm = comm.split(' ')
            func = comm[0]
            word = None
            if len(comm) > 1:
                word = comm[1]

            if func == 'L':
                self.L() 
            elif func == 'R':
                self.R()
            elif func == 'B':
                self.B()
            elif func == 'D':
                self.D()
            elif func == 'I':
                self.I(word=word)

        print(self)

    def I(self, word:str):
        node = Node(word, self.cursor.prev, self.cursor)
        self.cursor.prev.next = node
        self.cursor.prev = node

    def L(self):
        if self.cursor.prev is not self.head:
            self.cursor.prev.next = self.cursor.next
            self.cursor.next.prev = self.cursor.prev
            self.cursor.next = self.cursor.prev
            self.cursor.prev = self.cursor.prev.prev
            self.cursor.prev.next = self.cursor
            self.cursor.next.prev = self.cursor

    def R(self):
        if self.cursor.next is not self.tail:
            self.cursor.next.prev = self.cursor.prev
            self.cursor.prev.next = self.cursor.next
            self.cursor.next = self.cursor.next.next
            self.cursor.prev = self.cursor.prev.next
            self.cursor.next.prev = self.cursor
            self.cursor.prev.next = self.cursor

    def B(self):
        if self.cursor.prev is not self.head:
            self.cursor.prev = self.cursor.prev.prev
            self.cursor.prev.next = self.cursor

    def D(self):
        if self.cursor.next is not self.tail:
            self.cursor.next = self.cursor.next.next
            self.cursor.next.prev = self.cursor

command = input('Enter Input : ')
vim = Vim()
vim.do(command)