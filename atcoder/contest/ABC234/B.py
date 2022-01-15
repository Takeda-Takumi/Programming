import math

n = int(input())
x = [0] * n
y = [0] * n

for i in range(n):
    x[i], y[i] = map(int, input().split())


# min_index = max((max(x) - min(x)), (max(y) - min(y)))
# if((max(x) - min(x)) > (max(y) - min(y))):
#     min_index = x.index(min(x))
# else:
#     min_index = y.index(min(y))

# max_lenghth = 0
# for i in range(n):
#     current_length = math.sqrt((x[i]-x[min_index])**2 + (y[i] - y[min_index])**2) 
#     if(current_length > max_lenghth):
#         max_lenghth = current_length
# print(max_lenghth)



max_lenghth = 0
count = 0
for i in range(n):
    for j in range(i+1, n, 1):
        count += 1;
        current_length = math.sqrt((x[i]-x[j])**2 + (y[i] - y[j])**2) 
        if(current_length > max_lenghth):
            max_lenghth = current_length
print(max_lenghth, count)