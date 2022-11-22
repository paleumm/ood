class Hash:
    def __init__(self, tableSize: int, maxCollision: int, threshold: int) -> None:
        self.table = [None]*tableSize
        self.maxCollision = maxCollision
        self.tableSize = tableSize
        self.threshold = threshold
        self.inserted = []
        self.collide = 0
        self.hashed = 0

        print("Initial Table :")
        self.printHashTable()

    def printHashTable(self):
        for i in range(1, self.tableSize + 1):
            print(f'#{i}	{self.table[i-1]}')
        print('----------------------------------------')

    def insert(self, data):
        self.hashed = 0
        self.collide = 0
        if data not in self.inserted: # print 'Add: data' when inserted new data ony
            self.inserted.append(data)
            print(f'Add : {data}')
        while True:
            idx = self.hashF(data, int(self.collide))
            if self.exceedThreshold(): # over threshold
                print(f'****** Data over threshold - Rehash !!! ******')
                self.rehash()
                return
            if self.collided(idx) and self.collide < self.maxCollision + 1: # collision case
                if self.collide < self.maxCollision:
                    print(f'collision number {self.collide+1} at {idx}')
                
                self.hashed += 1
                self.collide += 1

                if self.collide == self.maxCollision: # max collision
                    print('****** Max collision - Rehash !!! ******')
                    self.rehash()
                    return
            else: # case not collide or exceed threshold
                self.table[idx] = data
                break

        # print only when we insert new data only (when rehash)
        if data == self.inserted[-1]:
            self.printHashTable()



    def hashF(self, data, i=0) -> int:
        idx = data % self.tableSize
        idx = (idx + i*i) % self.tableSize
        return idx

    def collided(self, idx) -> bool:
        if self.table[idx] is not None:
            return True
        return False  

    def exceedThreshold(self) -> bool:
        count = 0
        for d in self.table:
            if d is not None:
                count += 1
            if count + 1 >= float(self.threshold* self.tableSize / 100):
                return True
        return False

    def nextPrime(self, num) -> int:
        while True:
            check = True
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    check = False
                    break
            if check:
                return num
            num += 1

    def rehash(self):
        self.tableSize = self.nextPrime(self.tableSize * 2)
        self.table = [None]*self.tableSize
        for d in self.inserted:
            self.insert(d)


print(' ***** Rehashing *****')
inp = input('Enter Input : ').split('/')
tableSz, maxColl, threshold = inp[0].split()
tableSz = int(tableSz)
maxColl = int(maxColl)
threshold = int(threshold)
data = inp[1].split()

h = Hash(tableSz, maxColl, threshold)

for d in data:
    h.insert(int(d))
