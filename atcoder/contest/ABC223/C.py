n = int(input())
a = [[] for i in range(n)]
b = [[] for i in range(n)]


doukasen_length = 0
for i in range(n):
    a[i], b[i] = map(int, input().split())
    doukasen_length += a[i]

left = -1
right = n+1

while True:
    mid = (left + right) / 2
    target_position = mid
    left_current_position = 0
    left_time = 0
    i = 0
    while left_current_position + a[i] < target_position:
        left_current_position += a[i]
        left_time += (a[i] / b[i])
        i += 1

    if(left_current_position != target_position):
        left_time += (target_position - left_current_position) / b[i]


    right_current_position = 0
    right_time = 0
    j = n-1
    while right_time + (a[j] / b[j]) < left_time:
        right_current_position += a[j]
        right_time += (a[j] / b[j])
        j -= 1

    if(right_time != left_time):
        right_current_position += (left_time - right_time) * b[j] 

    length = doukasen_length - target_position
    if(abs(length - right_current_position) < 10**(-16)):
        print(mid)
        break
    elif(length < right_current_position):
        right = mid
    else:
        left = mid






