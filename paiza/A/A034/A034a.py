# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import queue

n,x = (int(z) for z in input().split())
value = [int(input()) for i in range(n)]
min_change = 5000
max_itemcount = 0
q = queue.LifoQueue()

def dfs(i,v,itemcount):
    global min_change
    global max_itemcount
#    print("(i,v) =",i,v,"itemcount =",itemcount)
#    print(q.queue)
    if(i == n):
#        print("到達")
        if(max_itemcount < itemcount):
#            print("更新")
            max_itemcount = itemcount
            min_change = v
        elif(max_itemcount == itemcount and min_change > v):
#            print("更新")
            min_change = v
#        else:
#            print("更新なし")
#        print("max_itemcount =",max_itemcount,"min_change =",min_change)
#        print("return")
        return min_change
    elif(v < value[i]):
#        print(value[i],"が入らない")
        q.put(0)
        tmp = dfs(i+1,v,itemcount)
        q.get()
        return tmp    
    else:
#        print("残り",v)
#        print(value[i],"を入れない")
        q.put(0)
        res1 = dfs(i+1,v,itemcount)
        q.get()
#        print("残り",v)
#        print(value[i],"を入れる")
        q.put(value[i])
        res2 = dfs(i+1,(v - value[i]),itemcount+1)
        if(res1 > res2):
            min_res = res2
        else:
            min_res = res1
        q.get()
#        print("res1 =",res1,"res2 =",res2)
#        print("min =",min_res)
#        print("return")
        return min_res

print(dfs(0,x,0))