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