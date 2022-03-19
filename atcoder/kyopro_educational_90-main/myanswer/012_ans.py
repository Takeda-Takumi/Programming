from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


h, w = (int(x) for x in input().split())
q = int(input())

qry = []
for i in range(q):
    qry.append([int(x) for x in input().split()])

square = [[False]*2009 for i in range(2009)]
uf = UnionFind(h*w)
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]


for i in range(q):
    if(qry[i][0] == 1):
        ri = qry[i][1]
        ci = qry[i][2]
        square[ri][ci] = True

        for dir in d:
            rid = ri+dir[0]
            cid = ci+dir[1]
            if(square[rid][cid]):
                hash1 = (ri-1)*w + (ci-1) 
                hash2 = (rid-1)*w + (cid-1)
                uf.union(hash1, hash2)

    else:
        xa, ya, xb, yb = qry[i][1] , qry[i][2] , qry[i][3] , qry[i][4]
        ans = "No"
        if(square[xa][ya] == False or square[xb][yb] == False):
            pass
        else:
            hash1 = (xa-1)*w + (ya-1) 
            hash2 = (xb-1)*w + (yb-1)
            if(uf.same(hash1, hash2)):
                ans = "Yes"
        print(ans)

