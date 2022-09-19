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
    
    def reverse(self):
        if not self.isEmpty():
            self.items.reverse()

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

def asteroid_collision(asts: list) -> list:
    s1 = Stack(asts)
    s2 = Stack()
    # _, out = recur(stk, Stack())
    # out = out.reverse()
    def recur(s1: Stack, s2: Stack):
        if s2.isEmpty() and not s1.isEmpty() :
            s2.push(s1.pop())

        if len(s1) == 0:
            return
        else:
            a1 = s1.pop()
            if (a1 > 0 and s2.peek() < 0): # same dir
                if abs(a1) == abs(s2.peek()): 
                    s2.pop()
                elif abs(a1) > abs(s2.peek()): 
                    s2.pop()
                    s1.push(a1)
                    recur(s1,s2)
                    return
            else:
                s2.push(a1)
        recur(s1,s2)
    
    recur(s1, s2)

    s2.reverse()
    return s2


x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))

