import copy
from operator import itemgetter
h, w = (int(x) for x in input().split())
s = [input() for i in range(h)]
list = []
sima = copy.copy(s)

sima_h = h + 2
sima_w = w + 2

sima.insert(h, '.'*w)
sima.insert(0, '.'*w)

'''
for i in range(sima_h):
    print(sima[i])
'''
for i in range(sima_h):
    sima[i] = '.' + sima[i] + '.'
'''
print()
for i in range(sima_h):
    print(sima[i])
print()
'''

sima_conut = 0
kaigan_count = 0
done = [[0]*sima_w for i in range(sima_h)]
'''
for i in range(sima_h):
    print(done[i])

print()
print("------------------------------------")
print()
'''


def search(i, j):
    global sima
    global done
    global sima_h
    global sima_w
    global sima_conut
    global kaigan_count

#    print("kaigan_count =",kaigan_count)

    if(sima[i][j] == '#' and done[i][j] == 0):
        done[i][j] = 1
        sima_conut += 1
        '''
        for k in range(sima_h):
            print(done[k])
        
        print()
        '''
        search(i, j+1)
        search(i-1, j)
        search(i, j-1)
        search(i+1, j)

        tmp = 0
        if(sima[i][j+1] == '#'):
            #            print("右")
            tmp += 1
        if(sima[i-1][j] == '#'):
            #            print("上")
            tmp += 1
        if(sima[i][j-1] == '#'):
            #            print("左")
            tmp += 1
        if(sima[i+1][j] == '#'):
            #            print("下")
            tmp += 1

        kaigan_count += (4-tmp)
#        print("探索開始","(",i,",",j,")の海岸数 :",4-tmp," kaigan_count =",kaigan_count)

        return 1

    return 0


for i in range(sima_h):
    for j in range(sima_w):
        #        print("(i,j) =",i,j)
        sima_conut = 0
        kaigan_count = 0
        if(sima[i][j] == '#' and done[i][j] == 0):
            #            print("探索開始","(",i,",",j,")")
            search(i, j)
            '''
            print("sima_count =",sima_conut,"kaigan_count =",kaigan_count)
            for k in range(sima_h):
                print(done[k])
            print()
            '''
            list.append([sima_conut, kaigan_count])
        else:
            continue


list.sort(key=itemgetter(1), reverse=True)

list.sort(key=itemgetter(0), reverse=True)


'''
for i in range(sima_h):
    print(done[i])
'''
if not list:
    print(0, 0)
else:
    for i in range(len(list)):
        print(list[i][0], list[i][1])
