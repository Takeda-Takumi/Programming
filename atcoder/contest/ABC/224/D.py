m = int(input())

u = [0 for i in range(m)]
v = [0 for i in range(m)]

for i in range(m):
    u[i], v[i] = map(int, input().split())

p = [int(x) for x in input().split()]

sum = 0
for i in range(8):
    sum += p[i]

vacant_position = 45 - sum

position_to_koma = [-1 for i in range(10)]
for i in range(1,10):
    for j in range(8):
        if(p[j] == i):
            position_to_koma[i] = j + 1


g = [[] for i in range(10)]

for i in range(m):
    g[u[i]].append(v[i])
    g[v[i]].append(u[i])

def CheckGameClear():
    for i in range(1,9):
        if(position_to_koma[i] != i):
            return False
    return True


def dfs(vacant_posision):
    if(CheckGameClear()):
        return True

    for candidate_position in g[vacant_posision]:
        tmp = position_to_koma[candidate_position] 
        position_to_koma[candidate_position] = -1
        position_to_koma[vacant_posision] = tmp
        
        dfs(candidate_position)

        position_to_koma[vacant_posision] = -1
        position_to_koma[candidate_position] = tmp
    
    return False

if(dfs(vacant_position)):
    print("yes")
else:
    print("No")

print()