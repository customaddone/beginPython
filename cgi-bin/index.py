n, k = map(int, input().split())
a = list(map(int, input().split()))

for bit in range(1 << n):
    sum = 0
    for i in range(n):
        # bit と 0b1000..の論理積
        # 合っていればTrue
        if bit & (1 << i):
            sum += a[i]
    if sum == k:
        print("Yes")
        exit()

if dfs(0, 0):
    print("Yes")
else:
    print("No")
