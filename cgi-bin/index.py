from copy import deepcopy

N, K = map(int, input().split())
P = [list(map(int, input().split())) for i in range(N)]

d = [0] * (1 << N)
for bit in range(1 << (N)):
    p = []
    for j in range(N):
        if bit & (1 << j):
            p.append(P[j])

    res = 0
    for x1, y1 in p:
        for x2, y2 in p:
            res = max(res, (x1 - x2) ** 2 + (y1 - y2) ** 2)

    d[bit] = res

# 数字のリスト
l = sorted(d)

def f(x):
    opt_d = [1 if i <= x else float('inf') for i in d]
    dp = deepcopy(opt_d)

    for bit in range(1 << N):
        j = bit
        while j:
            dp[bit] = min(dp[bit], dp[j] + dp[bit ^ j])
            j -= 1
            j &= bit

    return dp[-1] <= K

ok = len(l)
ng = 0
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if f(l[mid]):
        ok = mid
    else:
        ng = mid

print(l[ok])
