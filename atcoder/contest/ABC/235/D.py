from os import curdir
import queue
from tkinter.tix import Tree

a, n = (int(x) for x in input().split())

x = 1

q = queue.Queue()
next_q =queue.Queue()


next_q.put(1)
count = 0

dict = {}
f = False

while not next_q.empty():
    q = next_q
    next_q = queue.Queue()
    while not q.empty():
        get_num = q.get()
        dict[get_num] = True
        mul_num = a*get_num

        if(mul_num == n):
            f = True
            break
        
        if(get_num >+ 10 and x % 10 != 0):
            swap_num = int(str(get_num)[-1] + str(get_num)[0:-1])
            if(swap_num == n):
                f = True
                break
            if not swap_num in dict and len(str(swap_num)) <= len(str(n)):
                dict[swap_num] = True
                next_q.put(swap_num)
        
        if not mul_num in dict and len(str(mul_num)) <= len(str(n)):
            dict[mul_num] = True
            next_q.put(mul_num)
    count += 1
    
if f:
    print(count)
else:
    print(-1)

