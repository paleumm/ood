class Stack():
    def __init__(self, ls=None, max=None) -> None:
        if ls is None:
            self.items = []
        else:
            self.items = ls
        self.limit = max

    def __str__(self):
        return str(self.items)

    def __getitem__(self, i:int):
        return self.items[i]

    def __len__(self) -> int:
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