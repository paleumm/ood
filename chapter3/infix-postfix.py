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

operators = '^*/+-'

class Conversion(Stack):
    def __init__(self, infix:str) -> None:
        super(Conversion, self).__init__()
        self.infix = infix

    def getCurrentRank(self) -> int:
        rank = 0
        if self.peek() == '(':
            rank = 1
        elif self.peek() == '^':
            rank = 4
        elif self.peek() in '*/':
            rank = 3
        elif self.peek() in '+-':
            rank = 2
        elif self.peek() == ')':
            rank = 0
        return rank
    
    def checkRank(self, op:str, rank:int) -> bool:
        if op in '+-' and rank < 2:
            return True
        if op in '*/' and rank < 3:
            return True     
        if op == '^' and rank < 4:
            return True
        if op == '(':
            return True
        
        return False
    
    def getRank(self, op:str) -> int:
        if op in '+-':
            return 2
        if op in '*/':
            return 3     
        if op == '^':
            return 4
        if op == '(':
            return 0
        if op == ')':
            return 7

    def solve(self):
        output = ""
        for index, char in enumerate(self.infix):
            if char in operators or char in '()':
                print(output, char)
                print(self.__str__())
                if self.isEmpty():
                    self.push(char)
                else:
                    currentRank = self.getCurrentRank()
                    if self.checkRank(char, currentRank):
                        self.push(char)
                    else:
                        while self.__len__() > 0 and self.getRank(self.peek()) >= self.getRank(char):
                            if self.peek() in '()':
                                break
                            else:
                                output += str(self.pop())
                        self.push(char)   
                print(self.__str__())
                print()
            else:
                output += char
                # if not self.isEmpty() and index == len(self.infix)-1:
                #     output += str(self.pop())
                

        while not self.isEmpty():
            if self.peek() in '()':
                    self.pop()
            else:
                output += str(self.pop())
                    
            # print(output, char,self.__str__())
        return output


inp = input('Enter Infix : ')
c = Conversion(inp)

print('Postfix : ', c.solve())