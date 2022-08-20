class Queue():
    def __init__(self, items=None, max=None, ) -> None:
        if items is None:
            self.items = []
        else:
            self.items = items
        
        self.max = max
    
    def __str__(self) -> str:
        return str(self.items)

    def __len__(self) -> int:
        return len(self.items)

    def __getitem__(self, i:int):
        return self.items[i]

    def isEmpty(self):
        return len(self) == 0

    def isFull(self):
        if self.max is not None:
            return len(self) == self.max
        else:
            return False

    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)

    def enQueue(self, x, index=None):
        if not self.isFull():
            if index is None:
                self.items.append(x)
            else:
                self.items.insert(index, x)

class Stack():
    def __init__(self, max=None, ls=None) -> None:
        if list is None:
            self.items = []
        else:
            self.items = ls
        self.limit = max

    def __str__(self):
        return str(self.items)

    def __getitem__(self, i:int):
        return self.items[i]

    def __len__(self):
        return len(self.items)

    def push(self, x):
        if not self.isFull():  
            self.items.append(x)

    def pop(self, index=-1):
        if not self.isEmpty():
            return self.items.pop(index)
        else:
            print("Stack is empty, no element pop")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def isEmpty(self):
        return self.__len__() == 0
    
    def isFull(self):
        return self.__len__() == self.limit

class color():
    def __init__(self):
        pass

    def solve(self):
        pass

    def normal(self):
        pass
    
    def mirror(self):
        pass

inp = input('Enter Input (Normal, Mirror) : ').split()
normal = inp[0]
mirror = inp[1]

