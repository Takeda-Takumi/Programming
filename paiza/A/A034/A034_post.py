# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n,x = (int(z) for z in input().split())
value = [int(input()) for i in range(n)]
min_change = 5000
max_itemcount = 0

def dfs(i,v,itemcount):
    global min_change
    global max_itemcount
    if(i == n):
        if(max_itemcount <itemcount):
            max_itemcount = itemcount
            min_change = v
        elif(max_itemcount == itemcount and v < min_change):
            min_change = v
    elif(v < value[i]):
        dfs(i+1,v,itemcount)    
    else:
        dfs(i+1,v,itemcount)
        dfs(i+1,(v - value[i]),itemcount+1)
    return
    


 
dfs(0, x, 0)
print(min_change)