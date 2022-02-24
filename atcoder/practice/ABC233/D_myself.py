from collections import deque
n, k = (int(x) for x in input().split())
a = [int(x) for x in input().split()]

memo = [[None] *(n+1) for i in range(n+1)]
def dfs(i, q):
    queue = deque()
    ans = 0
    q.append(a[i])
    if(sum(list(q)) == k):
        ans += 1
    if(i >= n-1):
        return ans
    
    
    ans += dfs(i+1, q)
    q.popleft()
    ans += dfs(i+1, q)
    return ans


print(dfs(0)


