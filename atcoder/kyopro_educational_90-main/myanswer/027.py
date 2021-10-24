n = int(input())
s = [input() for i in range(1,n+1)]

usename_list = {}

for i in range(n):
    if(not (s[i] in usename_list.keys())):
        print(i+1)
        usename_list[s[i]] = 1
    
