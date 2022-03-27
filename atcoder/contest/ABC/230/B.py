s = input()

n = 10**2
t = "oxx" * n
ans = "No"
for i in range(3 * n - len(s)):
    #print("t=", t[i:i+len(s)])
    if(t[i:(i+len(s))] == s):
        ans = "Yes"

print(ans)

