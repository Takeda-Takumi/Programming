n = int(input())

for i in range(1<<n):
    s = ""
    sum = 0
    for j in range(n):
        if((i>>(n-j-1)) & 1):
            s += ")"
            sum -= 1   
        else:
            s += "("
            sum += 1
        if(sum < 0 or sum > n/2 or sum < -n/2):
            break
    
    if(sum == 0 and j == n-1):
        print(s)