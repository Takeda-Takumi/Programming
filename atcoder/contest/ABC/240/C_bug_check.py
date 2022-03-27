import random
ans1 = "a"
ans2 = "a"
while(ans1 == ans2):
    n = random.randint(1,10)

    a = []
    b = []
    for i in range(n):
        tmp_b = -1
        tmp_a = 1
        while(tmp_b < tmp_a):
            tmp_a = random.randint(1,100)
            tmp_b = random.randint(1,100)
        a.append(tmp_a)
        b.append(tmp_b)

    x = random.randint(1, 100)

    print("n =", n)
    print("a =", a)
    print("b =", b)
    print("x =", x)
    # -------------------------------------

    d = [-1] * (x+1)
    d[0] = 0
    for i in range(n):
        for j in range(x):
            if(d[j] == i): 
                if(j+a[i] <= x):
                    d[j+a[i]] = i+1
                if(j+b[i] <= x):
                    d[j+b[i]] = i+1

    if(d[x] == i+1):
        ans1 = "Yes"
    else:
        ans1 = "No"


    # ----------------------------
    ans2 = "No"
    for i in range(2**n):
        sum = 0
        for j in range(n):
            if ((i>>j) & 1):
                sum += a[j]
            else:
                sum += b[j]

        if sum == x:
            ans2 = "Yes"
            break
    
    print(ans1, ans2)
print()

