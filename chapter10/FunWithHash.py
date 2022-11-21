class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self, tableSize: int, maxCollision: int) -> None:
        self.table = [None]*tableSize
        self.maxCollision = maxCollision
        self.tableSize = tableSize
        self.num = 0
        self.h = 0

    def printHashTable(self) -> str:
        for i in range(1, self.tableSize + 1):
            print(f'#{i}	{self.table[i-1]}')
        print('---------------------------')

    def hashing(self, value: Data):
        idx, data = self.hashFunction(value)
        # print(data)
        if self.collided(data, idx):
            # if self.num == self.maxCollision:
            idx, data = self.quadProbe(value=value)
            if idx == -999:
                self.printHashTable()
                return
        self.h += 1
        self.table[idx] = data
        self.printHashTable()
        if self.h >= self.tableSize:
            print('This table is full !!!!!!')
            exit(0)

    def collided(self, value: Data, idx):
        if self.table[idx] is not None:
            return True
        return False  

    def hashFunction(self, value: Data) -> Data:
        key = value.key
        sum = 0
        for ch in key:
            sum += ord(ch)
        idx = sum % self.tableSize
        return idx, value

    def quadProbe(self, value: Data):
        idx, data = self.hashFunction(value)
        for i in range(self.tableSize):
            temp = (idx + i*i) % self.tableSize
            if not self.collided(data, temp):
                self.num = 0
                return temp, data
            else:
                self.num += 1
                print(f'collision number {self.num} at {temp}')
            if self.num == self.maxCollision:
                print('Max of collisionChain')
                self.num = 0
                return -999, None
        return -999, None


print(' ***** Fun with hashing *****')
inp = input('Enter Input : ').split('/')
tableSz, maxColl = inp[0].split()
data = inp[1].split(',')

dataIn = []

for i in data:
    key, val = i.split()
    d = Data(key=key, value=val)
    dataIn.append(d)
h = hash(int(tableSz), int(maxColl))

for d in dataIn:
    h.hashing(d)
