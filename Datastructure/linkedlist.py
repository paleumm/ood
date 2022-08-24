class Node:
    def __init__(self, data, next:Node = None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f'{self.data}'

class LinkedList:
    def __init__(self, head=None):
        if head is None:
            self.head = self.tail = None
            self.length = 0
        else:
            self.head = head
            temp = self.head
            self.length = 1
            while temp.next is not None:
                temp = temp.next
                self.length += 1
            self.tail = temp

    def isEmpty(self):
        return self.head is None

    def append(self, node:Node):
        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def __str__(self) -> str:
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, f'{self.head.data} '
        while cur.next is not None:
            s += f'{cur.next.data} '
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

        if idx == 0: # remove head
            self.head = self.head.next

        else:
            pass
        self.length -= 1

    def insert(self, x:Node, idx=None):
        if idx >= self.length:
            return None

        if idx is None or idx == self.length - 1:
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