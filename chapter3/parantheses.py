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
        
    def isMatch(self, op, cp):
        return openParan.index(op) == closeParan.index(cp)

    def solve(self):
        error = 0
        for char in self.string:
            if error != 0:
                break
            if char in openParan:
                self.push(char)
            else:
                if char in closeParan:
                    if not self.isEmpty() > 0:
                        if not self.isMatch(self.pop(), char):
                            error = 1
                    else:
                        error = 2

        if not self.isEmpty() and error == 0:
            error = 3
        return error, self.items


i = input('Enter expresion : ')
check = PCheck(i)
err,s = check.solve()
if err == 0:
    print(i, 'MATCH')
elif err == 1:
    print(i, 'Unmatch open-close')
elif err == 2:
    print(i, 'close paren excess')
elif err == 3:
    print(i,f'open paren excess   {len(check)} :',"".join(s))
    

