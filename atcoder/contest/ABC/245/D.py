n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

b = [0] * (m+1)


for i in range(n+m+1):
    sum = 0
    for j in range(n+1):
        for k in range(m+1):
            if(j+k == i):
                sum += c[i] / a[j]
    b[i] = sum

for nx in b:
    print(nx, "", end="")
print()


    



    
