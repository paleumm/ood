class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
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

    def __str__(self) -> str:
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, f'{self.head.data} '
        while cur.next is not None:
            s += f'{cur.next.data} '
            cur = cur.next
        return s

    def __len__(self):
        return self.length

    def isEmpty(self):
        return self.head is None

    def append(self, data):
        node = Node(data)
        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def insert(self, index, data):
        node = Node(data)