n, x = (int(z) for z in input().split())
value = [int(input()) for i in range(n)]
corrent_sum = 0
corrent_itemcount = 0

for i in range(2 ** n):
    #    print(bin(i))
    sum = 0
    itemcount = 0
    for j in range(n):
        if((i >> j) & 1):
            if(sum + value[j] <= x):
                sum += value[j]
                itemcount += 1
            else:
                break
#    print("sum =",sum,"corrent_sum =",corrent_sum)
        #        print("sum <= x")
    if(corrent_itemcount < itemcount):
        #            print("sumを更新")
        corrent_itemcount = itemcount
        corrent_sum = sum
    elif(corrent_itemcount == itemcount and corrent_sum < sum):
        #            print("sumを更新")
        corrent_sum = sum
#        else:
#            print("sumを更新しない")

#    else:
#        print("sum > x")

#    print("corrent_itemcount =",corrent_itemcount,"corrent_sum =",corrent_sum)

print(x - corrent_sum)
