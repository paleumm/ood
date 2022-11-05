class Team:
    def __init__(self, name: str, wins: int, loss: int, draws: int, scored: int, conceded: int) -> None:
        self.name = name
        self.wins = wins
        self.loss = loss
        self.draws = draws
        self.scored = scored
        self.conceded = conceded

    def __str__(self) -> str:
        t = {'points': (self.wins*3 + self.draws*1)}
        gd = {'gd': (self.scored - self.conceded)}
        return f'[\'{self.name}\', {t}, {gd}]'
    
    def __lt__(self, other):
        score_A = (self.wins*3 + self.draws*1)
        scon_A = self.scored - self.conceded
        score_B = (other.wins*3 + other.draws*1)
        scon_B = other.scored - other.conceded

        if score_A == score_B:
            return scon_A < scon_B
        return score_A < score_B

def mergesort(L : list):
    if len(L) > 1: # not base case
        mid = len(L) // 2
        
        LL = L[:mid]
        RL = L[mid:]

        mergesort(LL)
        mergesort(RL)


        i = 0
        j = 0
        k = 0

        while i < len(LL) and j < len(RL):
            if LL[i] < RL[j]:
                L[k] = LL[i]
                i += 1
            else:
                L[k] = RL[j]
                j += 1

            k += 1

        while i < len(LL):
            L[k] = LL[i]
            i += 1
            k += 1

        while j < len(RL):
            L[k] = RL[j]
            j += 1
            k += 1

    return L

def printTeam(tt: Team):
    s = '['
    s += '\''
    s += tt.name
    s += '\''
    s += ', {\'points\': '
    s += str(tt.wins*3 + tt.draws*1)
    s += '}, {\'gd\': '
    s += str(tt.scored - tt.conceded)
    s += '}]'
    return s


    
inp = input('Enter Input : ').split('/')

T = []

for i in inp:
    ii = i.split(',')
    t = Team(ii[0],int(ii[1]),int(ii[2]),int(ii[3]),int(ii[4]),int(ii[5]))
    T.append(T)

print(T)

print("== results ==")

T = mergesort(T)