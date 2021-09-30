a,b,n = (int(x) for x in input().split())


p = []
for x  in input().split():
    if(x == 'G'):
        p.append(0)
    else:
        p.append(int(x))

#print(a,b,n)
#print(p)

score_sum = 0
score = 0
counter = 0
count = 0

for i in range(n):
    #print("i+1 =",i+1," ","p[",i,"] =",p[i]," counter =",counter," score_sum =",score_sum)
    score += p[i]

    if(i == n-1):
        score_sum += score
        break

    if(score == b):
        if(counter == 0):
            score += p[i+1] + p[i+2]
            if(i+3 != n):
                counter +=1
#            print(score)
            score_sum += score
            score = 0
        else:
            score += p[i+1]
#            print(score)
            score_sum += score
            score = 0
    elif(counter == 1):
#        print(score)
        score_sum += score
        score = 0
    counter = (counter+1)%2

    
print(score_sum)