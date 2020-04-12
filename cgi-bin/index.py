import bisect
n = int(input())
l = sorted(list(map(int, input().split())))
counter = 0
for i in range(n):
    for j in range(i + 1, n):
        counter += (bisect.bisect_left(l, l[i] + l[j]) - j - 1)
print(counter)
