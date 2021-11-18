import random

n = 0
x = 0
value = []



def rand():
    global n , x
    global value
    value = []
    n = random.randint(1, 20)
    x = random.randint(1, 5000)

    for i in range(n):
        value.append(random.randint(1, 5000))

def test():
    global n, x
    global value
    '''
    n = 3
    x = 300
    value = [150, 130, 120]
    '''
    n = 5
    x = 2967
    value = [99, 4019, 2310, 3792, 2454]


def dfs(i,v,itemcount,min_change, max_itemcount):
    if(i == n):
        if(max_itemcount <itemcount):
            max_itemcount = itemcount
            min_change = v
        elif(max_itemcount == itemcount and v < min_change):
            min_change = v
    elif(v < value[i]):
        min_change, max_itemcount = dfs(i+1,v,itemcount, min_change, max_itemcount)    
    else:
        min_change, max_itemcount = dfs(i+1,v,itemcount, min_change, max_itemcount)
        min_change, max_itemcount = dfs(i+1,(v - value[i]),itemcount+1, min_change, max_itemcount)
    return min_change, max_itemcount

def B():
    corrent_sum = 0
    corrent_itemcount = 0

    for i in range(2 ** n):
        sum = 0
        itemcount = 0
        for j in range(n):
            if((i >> j) & 1):
                if(sum + value[j] <= x):
                    sum += value[j]
                    itemcount += 1
                else:
                    break
        if(corrent_itemcount < itemcount):
            corrent_itemcount = itemcount
            corrent_sum = sum
        elif(corrent_itemcount == itemcount and corrent_sum < sum):
            corrent_sum = sum

    return x - corrent_sum






rand()
test()





for i in range(100):
    print()
    print("初期値")
    print(n,x)
    print(value)
    a, _ = dfs(0, x, 0, 5000, 0)
    b = B()
    print("a, b = ", a, b)
    if(a == b):
        print("合ってる")
        rand()
        continue
    else:
        print("間違い")
        break

if(i == 99):
    print("ok")







