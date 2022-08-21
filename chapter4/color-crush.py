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
    def reverse(self):
        if not self.isEmpty():
            self.items.reverse()
    def peek(self):
        if not self.isEmpty():
            return self[0]

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

    def reverse(self):
        if not self.isEmpty():
            self.items.reverse()

class color():
    def __init__(self, normal:list, mirror):
        self.normalQ = Queue(normal)

        self.mirrorQ = Queue(mirror)
        self.mirrorQ.reverse()
       
        self.normalB = Queue()
        self.mirrorB = Queue()
        self.normalS = Stack()
        self.mirrorS = Stack()
        self.normalCount = 0
        self.mirrorCount = 0

    def solve(self):
        self.mirror()
        ex, fail = self.normal()

        print('NORMAL : ')
        self.normalS.reverse()
        print(len(self.normalS))

        if self.normalS.isEmpty():
            print('Empty')
        else:
            print("".join(self.normalS))

        print(f'{ex} Explosive(s) ! ! ! (NORMAL)')
        if fail > 0:
            print(f'Failed Interrupted {fail} Bomb(s)')

        print('------------MIRROR------------')
        print(': RORRIM')
        print(len(self.mirrorS))
        if len(self.mirrorS) > 0:
            print(''.join(self.mirrorS))
        else:
            print('ytpmE')
        print(f'(RORRIM) ! ! ! (s)evisolpxE {self.mirrorCount}')

    def normal(self):
        normalB, normalS = self.bomb(self.normalQ)
        num_normalB = len(normalB)
        num_mirrorB = len(self.mirrorB)

        normalB_interrupted = self.addInterrupt(self.mirrorB, self.normalQ, normalB, normalS)
        self.normalB, self.normalS = self.bomb(normalB_interrupted)

        num_bomb = len(self.normalB)

        fail = 0
        explode = 0
        
        if self.normalB.isEmpty():
            return explode, fail

        if num_normalB > num_bomb:
            explode = num_bomb
        elif num_bomb == num_normalB:
            fail = num_mirrorB
            explode = num_bomb - fail
        elif num_bomb > num_normalB:
            fail = num_bomb - num_normalB
            explode = num_bomb - fail
       
        return explode, fail
        

    def mirror(self):
        self.mirrorB, self.mirrorS = self.bomb(self.mirrorQ, isMirror=True)
        self.mirrorS.reverse()

    # normalQ -> normal input, bombQ -> queue of bomb in normal
    def addInterrupt(self, interrupt:Queue, normalQ:Queue, bombQ:Queue, bombS) -> Queue:
        if not interrupt.isEmpty():
            count = 0
            for idx, bomb in enumerate(normalQ):
                if bombQ.isEmpty() or interrupt.isEmpty():
                    break
                if bomb == bombQ.peek():
                    count += 1
                    if count == 3:
                        normalQ.enQueue(interrupt.deQueue(), idx)
                        count = 0
                        bombQ.deQueue()
                elif bomb != bombQ.peek() and count > 0:
                    count = 0
        return normalQ

    def bomb(self, q:Queue, isMirror=False, isInterrupted=False) -> Queue:
        bombS = Stack()
        bombQ = Queue()
        for b in q:
            if len(bombS) < 2:
                bombS.push(b)
            else:
                bombS.push(b)
                f, s ,t = bombS.pop(), bombS.pop(), bombS.pop()
                if f == s == t:
                    bombQ.enQueue(f)
                    if isMirror:
                        self.mirrorCount += 1
                    else:
                        self.normalCount += 1
                else:
                    bombS.push(t)
                    bombS.push(s)
                    bombS.push(f)
        return bombQ, bombS

inp = input('Enter Input (Normal, Mirror) : ').split()
normal = [*inp[0]]
mirror = [*inp[1]]

bomb = color(normal, mirror)
bomb.solve()