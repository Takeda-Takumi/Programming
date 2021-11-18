# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import queue

n,x = (int(z) for z in input().split())
value = [int(input()) for i in range(n)]
corrent_sum = 0
max_itemcount = 0
q = queue.LifoQueue()
def dfs(i,sum,itemcount):
    global corrent_sum
    global max_itemcount
    if(i == n):
        if(max_itemcount < itemcount):
            max_itemcount = itemcount
            corrent_sum = sum
        elif(max_itemcount == itemcount and corrent_sum < sum):
            corrent_sum = sum
        return corrent_sum
    elif(sum + value[i] > x):
        q.put(0)
        tmp = dfs(i+1,sum,itemcount)
        q.get()
        return tmp    
    else:
        q.put(0)
        res1 = dfs(i+1,sum,itemcount)
        q.get()
        q.put(value[i])
        res2 = dfs(i+1,(sum + value[i]),itemcount+1)
        if(res1 < res2):
            max_res = res2
        else:
            max_res = res1
        q.get()
        return max_res

print(x-dfs(0,0,0))