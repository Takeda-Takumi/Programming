import itertools

n = input()
list_n = list(n)
list_n_length = len(list_n)
p = itertools.permutations(list_n,list_n_length)

count = 0

max_value = 0
for v in itertools.permutations(list_n, list_n_length):
    for back_half_start in range(1, list_n_length-1):
        count += 1
        if(v[0] == '0'):
            continue 
        if(v[back_half_start] == '0'):
            continue

        replaced_n = "".join(v)
        if(back_half_start-1 == 0):
            front_half_int = int(replaced_n[0])
        else:
            front_half_int = int(replaced_n[0:back_half_start])
        
        if(back_half_start == list_n_length):
            back_half_int = int(replaced_n[list_n_length])
        else:
            back_half_int = int(replaced_n[back_half_start:list_n_length])

        multiplied =  front_half_int*back_half_int

        max_value = max(multiplied,max_value)

print(count)
print(max_value)


