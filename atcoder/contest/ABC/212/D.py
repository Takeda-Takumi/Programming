import heapq

q = int(input())
heap = []
heapq.heapify(heap)
ans = []
add = 0
for i in range(q):
    qry = [int(x) for x in input().split()]

    if(qry[0] == 1):
        heapq.heappush(heap, qry[1]-add)
    elif(qry[0] == 2):
        add += qry[1]
    else:
        ans.append(heapq.heappop(heap)+add)

for nx in ans:
    print(nx)
