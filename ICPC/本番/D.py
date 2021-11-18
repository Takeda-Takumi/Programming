n = int(input())
b = [int(x) for x in input().split()]

b.sort(reverse=True)

print()


while True:
    if(b.count(0) == n-2):
        break
    count = 0
    for i in range(n):
        if(b[i] != 0 and count != 3):
            b[i] -= 1
            count += 1
        if(count == 3):
            break
    

