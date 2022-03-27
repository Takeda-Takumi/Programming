a, b, c, d = map(int, input().split())

ans = "Aoki"
if(a < c):
    ans = "Takahashi"
elif(a > c):
    pass
elif(b < d):
    ans = "Takahashi"
elif(b > d):
    pass
else:
    ans = "Takahashi"

print(ans)
