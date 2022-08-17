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

class genSecret():
    def __init__(self, string:list, number:list) -> None:
        self.string = Queue(items=string)
        self.number = Queue(items=number)
        self.encodedmsg = Queue()
        self.decodedmsg = Queue()

    def encode(self):
        secret = self.string
        num = self.number
        while not secret.isEmpty():
            n = num.deQueue()
            num.enQueue(n)
            e = secret.deQueue()
            en = ''
            if e.islower():
                x = ((ord(e)-ord('a')) + n)%26
                en = chr(x+ord('a'))
            elif e.isupper():
                x = ((ord(e)-ord('A')) + n)%26
                en = chr(x+ord('A'))
            self.encodedmsg.enQueue(en)
        return list(self.encodedmsg)

    def decode(self):
        secret = self.string
        num = self.number
        while not secret.isEmpty():
            n = num.deQueue()
            num.enQueue(n)
            e = secret.deQueue()
            en = ''
            if e.islower():
                x = ((ord(e)-ord('a')) - n)%26
                en = chr(x+ord('a'))
            elif e.isupper():
                x = ((ord(e)-ord('A')) - n)%26
                en = chr(x+ord('A'))
            self.decodedmsg.enQueue(en)
        return list(self.decodedmsg)

inp = input('Enter String and Code : ').split(',')
strings = inp[0].split(' ')
string_in = []
for string in strings:
    for st in string:
        string_in.append(st)

num = [*inp[1]]
num = list(map(int, num))

e = genSecret(string=string_in, number=num)
encoded = e.encode()
print(f'Encode message is :  {encoded}')

num = [*inp[1]]
num = list(map(int, num))

d = genSecret(string=encoded, number=num)
decoded = d.decode()
print(f'Decode message is :  {decoded}')