class Stack():
    '''
    stack.py
    hello
    '''
    def __init__(self, list:list=None, limit=None) -> None:
        if list is None:
            self.items = []
        else:
            self.items = list
        self.limit = limit

    def __str__(self):
        return str(self.items)

    def __getitem__(self, i:int):
        return self.items[i]

    def __len__(self):
        return len(self.items)

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack is empty, no element pop")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def isEmpty(self):
        return self.__len__() == 0


print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:
    s.push(e)

print(len(s),"Data in stack : ",s.items)

while not s.isEmpty():
    s.pop()

print(len(s),"Data in stack : ",s.items)