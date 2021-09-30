a, b, n = (int(x) for x in input().split())
p = [x for x in input().split()]

p = [0 if i == 'G' else i for i in p]

for i in range(n):
    p[i] = int(p[i])

# print(a,b,n)
# print(p)

score_sum = 0
score = 0
counter = 0
count = 0

i = 0
while i < n:
    count += 1
    print("i =",i," ","p[",i,"] =",p[i]," counter =",counter," score_sum =",score_sum)
    if(i == n-1):
        score_sum += p[i]
        break 

    if(p[i] == b):
        score_sum += p[i] + p[i+1] + p[i+2]
        i += 1
    elif(p[i] + p[i+1] == b):
        score_sum += p[i] + p[i+1] + p[i+2]
        i += 2
    else:
        score_sum += p[i] + p[i+1]
        i += 2


print("count =",count)
print(score_sum)
