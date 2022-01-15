l, r = (int(x)-1 for x in input().split())
s = input()

if(len(s) == (r-l)+1):
    print(s[::-1])
else:
    tmp1 = s[l:r+1]
    tmp2 = tmp1[::-1]
    print(s[:l] + tmp2 + s[r+1:])