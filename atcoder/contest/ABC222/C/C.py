from operator import itemgetter

n, m = (int(x) for x in input().split())
a = [input() for i in range(2*n)]

rank = [[i,0] for i in range(2*n)] # 左が人ごとに割り当てられた番号、右が勝数

def isWinner(ronud, player1, player2): #player1の勝敗を返す
    player1_hand = a[player1][ronud]
    player2_hand = a[player2][ronud]
    if(player1_hand == player2_hand):
        return 0
    elif(player1_hand == 'G'and player2_hand == 'C'):
        return 1
    elif(player1_hand == 'C' and player2_hand == 'P'):
        return 1
    elif(player1_hand == 'P' and player2_hand == 'G'):
        return 1
    else:
        return -1


for round in range(0,m):
    for k in range(0, n):
        current_rank_index1 = 2*k
        current_rank_index2 = 2*k + 1
        current_player1 = rank[current_rank_index1][0]
        current_player2 = rank[current_rank_index2][0]
        result = isWinner(round, current_player1, current_player2)
        if(result == 1):
            rank[current_rank_index1][1] += 1
        elif(result == -1):
            rank[current_rank_index2][1] += 1

    rank.sort(key=itemgetter(0))
    rank.sort(key=itemgetter(1), reverse=True)

for x in rank:
    print(x[0]+1)



