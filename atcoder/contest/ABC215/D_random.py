import random

res = []
ans = []
while(res == ans):
    # n, m = map(int, input().split())
    # a = [int(x) for x in input().split()]
    n = random.randint(1, 10)
    m = random.randint(1, 10)
    a = [random.randint(1, 10) for i in range(n)]
    size = 10**5 + 5

    def pfact(x):
        res = []
        for i in range(2, int(x**(0.5))+1):
            while(x%i==0):
                x //= i
                res.append(i)
        if(x != 1):
            res.append(x)
        return res

    fl = [True] * size

    for i in range(n):
        v = pfact(a[i])

        for nx in v:
            if(fl[nx]):
                for j in range(nx, size, nx):
                    fl[j] = False

    res1 = []
    for i in range(1, m):
        if(fl[i]):
            res1.append(i)

    # print(len(res))

    # for nx in res:
    #     print(nx)

    # --------------------------------------------------------------

    # 約数をdivに加える
    def make_divisors(n):
        i = 1
        while i*i <= n:
            if n % i == 0:
                div.add(i)
                if i != n // i:
                    div.add(n//i)
            i += 1
        return


    N, M = n, m

    A = a

    # 約数列挙
    div = set()

    # Aiの約数を求める
    for i in range(N):
        make_divisors(A[i])

    # set型divから配列ansへ変換
    Div = list(div)

    # 答えの配列(1~M)
    res = [True for i in range(M)]

    # 約数の倍数をFalseに
    for i in range(len(Div)):
        # Div[i]が1ならスキップ
        if Div[i] == 1:
            continue
        k = 1
        while Div[i] * k <= M:
            res[Div[i] * k - 1] = False
            k += 1

    # 解答の配列(1は加えておく)
    ans = [1]
    for k in range(1,M):
        # resがTrueならINDEXをansに追加
        if res[k]:
            ans.append(k+1)

    #答えの数と値を出力
    # print(len(ans))
    # for i in range(len(ans)):
    #     print(ans[i])

print(n)
print(m)
print(a)

print("my")
print(res1)
print("other")
print(ans)