n = int(input())

if(n >= 42):
    n += 1
n = str(n)
print("AGC","0"*(3-len(n)), n, sep='')