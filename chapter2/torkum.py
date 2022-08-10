class TorKum():
    def __init__(self, input) -> None:
        self.input = input
        self.list = []

    def start(self):
        for word in self.input:
            if word[0] == 'P':
                temp = word.split()
                self.list.append(temp[1])
                self.play()
            
            elif word[0] == 'R':
                self.restart()
            
            elif word[0] == 'X':
                exit(1)
            else:
                print(f'\'{word}\' is Invalid Input !!! ')
                exit(0)

    def restart(self):
        self.list = []
        print('game restarted')

    def play(self):
        if len(self.list) == 1:
            print(f'\'{self.list[0]}\' -> {self.list}')
            return
        check = self.check(self.list[-2], self.list[-1])
        if check:
            print(f'\'{self.list[-1]}\' -> {self.list}')
        else:
            print(f'\'{self.list[-1]}\' -> game over')

    def check(self, word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        
        if word1[-2:-1] == word2[0:1]:
            return True
        else:
            return False
        


print('*** TorKham HanSaa ***')
inp = input('Enter Input : ').split(',')
game = TorKum(input=inp)
game.start()
