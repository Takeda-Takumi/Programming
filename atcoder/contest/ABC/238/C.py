n = int(input())

# def f(x):
#     digitX = len(str(x))
#     if(digitX == 1):
#         return x
#     else:
#         return x - 10**(digitX-1) + 1

# ans = 0
# for i in range(1, n+1):
#     ans += f(i)

# print(ans % 998244353)

digitN = len(str(n))

ans = 0
if(n < 10):
    print((n*(n+1))/2)
else:
    for i in range(digitN):
        if(i == 0):
            ans += ((((10**(i+1)-1)-10**i+1))*(((10**(i+1)-1)-10**i+1)+1)) / 2
        elif(i == digitN-1):
            ans += (((n-10**i+1))*((n-10**i+1)+1)) / 2
        else:
            ans += ((((10**(i+1)-1)-10**i+1))*(((10**(i+1)-1)-10**i+1)+1)) / 2

print(int(ans % 998244353))