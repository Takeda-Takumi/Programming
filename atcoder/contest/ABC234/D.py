n, k = (int(x) for x in input().split())

p = list(map(int, input().split()))



for i in range(k,n+1):
    p_part = p[:i]
    p_part.sort()
    print(p_part[-k])