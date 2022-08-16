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

    
    
class Soi(Stack):
    def __init__(self, max, ls, op, car):
        super(Soi, self).__init__(max=max, ls=ls)
        self.op = op
        self.car = car 

    def checkCar(self, x):
        for car in self.items:
            if car == x:
                return True
        return False

    def arrive(self, x):
        if self.isFull():
            print(f'cannot {self.op} : Soi Full')
        elif self.checkCar(x):
            print(f'already in soi')
        else:
            self.push(x)
            print(f'arrive! : Add Car {self.car}')

    def depart(self, x):
        if self.isEmpty():
            print(f'cannot depart : Soi Empty')
        elif not self.checkCar(x):
            print(f'cannot depart : Dont Have Car {self.car}')
        else:
            self.pop(0)
            print(f'depart ! : Car {self.car} was remove')

    def solve(self):
        if self.items[0] == 0:
            self.pop()
        print(f'car {self.car} ', end='')
        if self.op == 'depart':
            self.depart(self.car)
        if self.op == 'arrive':
            self.arrive(self.car)
        print(self.__str__())

print('******** Parking Lot ********')
Input = input('Enter max of car,car in soi,operation : ').split()

ls = Input[1].split(',')
ls = list(map(int, ls))
s = Soi(int(Input[0]), ls, Input[2], int(Input[3]))
s.solve()