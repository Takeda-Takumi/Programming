from numpy import square


h, w = (int(x) for x in input().split())
q = int(input())

qry = []
for i in range(q):
    qry.append([int(x) for x in input().split()])

square = [[False]*w for i in range(h)]
link = {}

d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for i in range(q):
    if(qry[i][0] == 1):
        ri = qry[i][1]
        ci = qry[i][2]
        square[ri][ci] = True

        for dir in d:
            rid = ri+d[0]
            cid = ci+d[1]
            if(square[[rid][cid]]):
                link[(ri, ci)] = ()


    else:
        pass



print()

