import bisect

h, w, n = map(int, input().split())

a = [0] * (n+1)
b = [0] * (n+1)
a_set = set()
b_set = set()
for i in range(1, n+1):
    a[i], b[i] = map(int, input().split())
    a_set.add(a[i])
    b_set.add(b[i])

a_sort = sorted(list(a_set))
b_sort = sorted(list(b_set))

for i in range(1, n+1):
    print(bisect.bisect_left(a_sort, a[i])+1, bisect.bisect_left(b_sort, b[i])+1)

# a = [0] * (n+1)
# b = [0] * (n+1)
# for i in range(1, n+1):
#     a[i], b[i] = map(int, input().split())


# a_sort = sorted(a)
# b_sort = sorted(b)

# for i in range(1, n+1):
#     print(bisect.bisect_left(a_sort, a[i]), bisect.bisect_left(b_sort, b[i]))


    