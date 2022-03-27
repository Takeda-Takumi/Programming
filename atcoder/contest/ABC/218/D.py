n = int(input())

x = [-1] * n
y = [-1] * n

dict = {}
for i in range(n):
    x[i], y[i] = map(int, input().split())
    dict[(x[i], y[i])] = True

count = 0
for i in range(n):
    for j in range(i+1, n):
        if x[i] == x[j] or y[i] == y[j]:
            continue
        lower_right_x = x[j]
        lower_right_y = y[i]

        upper_left_x = x[i]
        upper_left_y = y[j]

        lower_right_tuple = lower_right_x, lower_right_y
        upper_left_tuple = upper_left_x, upper_left_y

        if(lower_right_tuple in dict and upper_left_tuple in dict):
            count += 1

print(count//2)

 
