s = input()
t = input()

answer = 'No'

if(s == t):
    answer = 'Yes'

for i in range(len(s)-1):
    replace_list = list(s)
    replace_list[i] = s[i+1]
    replace_list[i+1] = s[i]
    replace_str = "".join(replace_list)
    if(replace_str == t):
        answer = 'Yes'
        break

print(answer)
