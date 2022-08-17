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

    def enQueue(self, x):
        if not self.isFull():
            self.items.append(x)

class QueueSolver(Queue):
    def __init__(self, inp:str, items=None, max=None,) -> None:
        super().__init__(items, max)

        self.inp = inp.split(',')

    def solve(self):
        for data in self.inp:
            if len(data) > 1:
                data = data.split(' ')

            if data[0] == 'D':
                if self.isEmpty():
                    print(-1)
                else:
                    out = self.deQueue()
                    print(f'Pop {out} size in queue is {len(self)}')
                
            elif data[0] == 'E':
                num = int(data[1])
                self.enQueue(num)
                print(f'Add {data[1]} index is {len(self) - 1}')
        output = '\', \''.join([str(st) for st in self.items])
        if not self.isEmpty():
            print(f'Number in Queue is :  [\'{output}\']')
        else:
            print('Empty')
        # output = ', '.join([str(st) for st in self.items])

inp = input('Enter Input : ')
q = QueueSolver(inp)
q.solve()
    