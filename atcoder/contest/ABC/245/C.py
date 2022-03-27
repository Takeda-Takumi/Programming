n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

af = True
bf = True
ans = "Yes"
for i in range(n-1):
    pre_af = af
    pre_bf = bf
    tmp_af = False
    tmp_bf = False
    if(pre_af):
        if(abs(a[i] - a[i+1]) <= k):
            tmp_af = True
        else:
            tmp_af = False

        if(abs(a[i] - b[i+1]) <= k):
            tmp_bf = True
        else:
            tmp_bf = False
        
    if(pre_bf):
        if(abs(b[i] - a[i+1]) <= k):
            tmp_af = True
        else:
            if(tmp_af != True):
                tmp_af = False

        if(abs(b[i] - b[i+1]) <= k):
            tmp_bf = True
        else:
            if(tmp_bf != True):
                tmp_bf = False

    af = tmp_af
    bf = tmp_bf

    if((not af) and (not bf)):
        ans = "No"
        break

print(ans)


