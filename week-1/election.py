print('*** Election ***')
num_vote = int(input('Enter a number of voter(s) : '))
votes = input()

votes = votes.split()
votes = list(map(int, votes))
if len(votes) != num_vote:
    exit()

vote_count = [0 for i in range(0,20)]

for vote in votes:
    if vote > 20 or vote < 1:
        continue

    vote_count[vote-1] += 1

max_count = max(vote_count)
max_check = 0
max_idx = []

for i in range(0,20):
    if vote_count[i] == max_count:
        max_check += 1
        max_idx.append(i)

if max_check > 1 or max_check <= 0:
    print('*** No Candidate Wins ***')
else:
    print(max_idx[0]+1)
