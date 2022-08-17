class Stack():
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

operators = '+-*/^'
paran = '()'

class Conversion(Stack):
    def __init__(self, infix:str) -> None:
        super(Conversion, self).__init__()
        self.infix = infix

    def getCurrentRank(self) -> int:
        rank = 0
        if self.peek() == '^':
            rank = 3
        elif self.peek() in '*/':
            rank = 2
        elif self.peek() in '+-':
            rank = 1
        return rank
    
    def getRank(self, op:str) -> int:
        if op in '+-':
            return 1
        if op in '*/':
            return 2     
        if op == '^':
            return 3
        if op in '()':
            return 0

    def solve(self):
        output = ""
        for ch in self.infix:
            if ch not in operators and ch not in paran:
                output += ch
            else:
                if self.isEmpty():
                    self.push(ch)
                else:
                    if ch in paran:
                        self.push(ch)
                        if ch == ')':
                            self.pop()
                            while not self.isEmpty():
                                if self.peek() == '(':
                                    self.pop()
                                    break
                                else:
                                    output += str(self.pop())
                    else:
                        rank = self.getCurrentRank()
                        if self.getRank(ch) > rank:
                            self.push(ch)
                        elif self.getRank(ch) == rank:
                            output += str(self.pop())
                            self.push(ch)
                        else:
                            while not self.isEmpty() and self.getRank(self.peek()) >= self.getRank(ch):
                                output += str(self.pop())
                            self.push(ch)
        while not self.isEmpty():
            if self.peek() not in '()':
                output += str(self.pop())
            else:
                self.pop()
        return output

print(' ***Infix to Postfix***')
inp = input('Enter Infix expression : ')
c = Conversion(inp)

print('PostFix : ')
print(c.solve())