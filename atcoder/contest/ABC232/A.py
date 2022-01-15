s = input()
t = input()

pre = (ord(s[0]) - ord(t[0]))%26
ans = "Yes"
for i in range(len(s)):
    tmp = (ord(s[i]) - ord(t[i]))%26
    if(tmp != pre):
        ans = "No"
        break
    pre = (ord(s[i]) - ord(t[i]))%26

print(ans)

