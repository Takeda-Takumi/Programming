n = input()
abc = 100*int(n[0]) + 10*int(n[1]) + int(n[2])
bca = 100*int(n[1]) + 10*int(n[2]) + int(n[0])
cab = 100*int(n[2]) + 10*int(n[0]) + int(n[1])
print(abc + bca + cab)