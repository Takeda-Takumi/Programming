w, h = (int(x) for x in input().split())

k = w + h - 1


n = [[-1]*(w+1) for i in range(h+1)]

for i in range(1, w*h):
    input_data = input().split()
    n[int(input_data[0])][int(input_data[1])] = int(input_data[2])


left = [0 for i in range(h+1)]
top = [0 for i in range(w+1)]

for i in range(1, h+1):
    if(n[i][1] != -1):
        left[i] = 1



print()



