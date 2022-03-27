n = int(input())

x = [-1]*n
y = [-1]*n

for i in range(n):
    x[i], y[i] = map(int, input().split())

s = input()

linkedlist = {}

# ans = "No"
# for i in range(n):

#     if y[i] in linkedlist:
#         for content in linkedlist[y[i]]:
#             if((content[1] == "R" and content[0] < x[i]) and (s[i] == "L")):
#                 ans = "Yes"
#                 break
#             if((content[1] == "L" and content[0] > x[i]) and (s[i] == "R")):
#                 ans = "Yes"
#                 break

#         else:
#             linkedlist[y[i]].append([x[i], s[i]])
#     else:
#         linkedlist[y[i]] = []
#         linkedlist[y[i]].append([x[i], s[i]])
    
#     if(ans == "Yes"):
#         break

ans = "No"
for i in range(n):

    if y[i] in linkedlist:
        soeji = linkedlist[y[i]] 
        if((s[soeji] == "R" and x[soeji] <= x[i]) and (s[i] == "L")):
            ans = "Yes"
            break
        elif((s[soeji] == "L" and x[soeji] >= x[i]) and (s[i] == "R")):
            ans = "Yes"
            break
        else:
            if(s[i] == "R" and x[i] < x[soeji]):
                linkedlist[y[i]] = i
            elif(s[i] == "L" and x[i] > x[soeji]):
                linkedlist[y[i]] = i
    else:
        linkedlist[y[i]] = i
    

print(ans)