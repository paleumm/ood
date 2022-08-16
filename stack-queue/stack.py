

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

openParan = "([{"
closeParan = ")]}"

class PCheck(Stack):
    def __init__(self, string:str):
        super(PCheck, self).__init__()
        self.string = string
        self.paran = ""

    def extract(self):
        for char in self.string:
            if char in openParan or char in closeParan:
                self.paran += char

    def isMatch(self, op, cp):
        return openParan.index(op) == closeParan.index(cp)

    def solve(self):
        error = 0
        self.extract()
        for char in self.paran:
            if char in openParan:
                self.push(char)
            else:
                if char in closeParan:
                    if not self.isMatch(self.pop(), char):
                        error = 1
                        break

        if error == 0:
            print("Match")


                    
    
# s = Stack([1])
# print(len(s))
# print(s)
# s.pop()
# s.pop()
# print(s.peek())
# s.push(5)
# s.push(20)
# s.push(10)
# print(s)
# s.pop()
# print(s)
# print(s.peek())
# print(len(s))
# print(s[1])
inp = input()
check = PCheck(inp)
check.solve()