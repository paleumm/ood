class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self) -> None:
        pass


print(' ***** Fun with hashing *****')
inp = input('Enter Input : ').split('/')