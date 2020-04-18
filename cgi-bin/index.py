n, k = map(int, input().split())
a = list(map(int, input().split()))

for bit in range(1 << n):
    sum = 0

    for i in range(n):
        if bit & (1 << i):
            sum += a[i]
    if sum == k:
        print('Yes')
        exit()

print('No')
