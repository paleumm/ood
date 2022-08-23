from platform import node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.index = 0

    def __str__(self) -> str:
        return f'{self.index} {self.data} {self.next}'

class LinkedList:
    def __init__(self, node:Node=None, ls:list = None, format:str=" "):
        self.head = None
        self.tail = None
        self.length = 0
        self.format = format
        # if node is not None:
        #     self.head = node
        #     self.tail = node
        #     self.length += 1
        
    def isEmpty(self):
        return self.head is None

    def append(self, node:Node):
        # node.index = self.length
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

        self.length += 1

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        
        cur, s = self.head, f'{self.head.data} '
        while cur.next != None:
            # s += f'{cur.next.data}'
            s += f'{cur.next.data} '
            # if cur.next is not self.tail:
            #     s += f'{self.format}'
            cur = cur.next
        return s

    def index(self, x):
        if self.isEmpty():
            return -1
        
        cur = self.head
        idx = 0
        while cur is not None:
            if cur.data == x:
                return idx
            cur = cur.next
            idx += 1
        return -1

    def search(self, x)->bool:
        if self.isEmpty():
            return False
        
        cur = self.head
        while cur is not None:
            if cur.data == x:
                return True
            cur = cur.next
        return False
    
    def __len__(self):
        return self.length

    def pop(self, idx):
        if idx >= self.length:
            return None

        if idx == 0:
            self.head = self.head.next

        else:
            i = 0
            cur = self.head
            while cur is not None and i < idx:
                if i + 1 == idx:
                    cur.next
                    cur.next 

                cur = cur.next
                i += 1
        self.length -= 1


# length can be decreased if index out of range
    def insert(self, x:Node, idx=None):
        if idx >= self.length:
            return None

        if idx is None:
            self.append(x)
        else:
            if idx == 0:
                x.next = self.head
                self.head = x
            else:
                i = 0
                cur = self.head
                while cur is not None and i < idx:
                    if i + 1 == idx:
                        x.next = cur.next
                        cur.next = x

                    cur = cur.next
                    i += 1
        self.length += 1
                        


    def __getitem__(self, i:int):
        if self.isEmpty():
            return None
        
        cur = self.head
        idx = 0
        while cur is not None and idx <= i:
            if idx == i:
                return cur.data
            cur = cur.next
            idx += 1
        return None


l = LinkedList()
# print(l)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
l.append(n1)
l.append(n2)
l.append(n3)
n1 = Node(1)
n2 = Node(9)
n3 = Node(3)
l.append(n1)
l.append(n2)
l.append(n3)
print(l)
print(len(l))
print(l[4])
l.insert(Node(5), 9)
print(l)
print(len(l))