class LinkedStack:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def first(self):
        if self.isEmpty():
            raise Empty('Queue is empty')

        return self._head._element

    def dequeue(self):
        if self.isEmpty():
            raise Empty('Queue is empty')
        
        output = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.isEmpty():
            self._tail = None
        return output

    def enqueue(self, e):
        new = self._Node(e, None)
        if self.isEmpty():
            self._head = new
        else:
            self._tail._next = new

        self._tail = new
        self._size += 1