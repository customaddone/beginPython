n = 14
w = [8, 7, 1, 4, 3, 5, 4, 1, 6, 8, 10, 4, 6, 5]
# 未開発の部分は-1
dp = [[-1] * (n + 1) for i in range(n + 1)]

def rec(l, r):
    if dp[l][r] != -1:
        return dp[l][r]

    if abs(l - r) <= 1:
        return 0

    res = 0

    if abs(w[l] - w[r - 1]) <= 1 and rec(l + 1,r - 1) == r - l - 2:
        res = r - l
    for i in range(l + 1, r):
        res = max(res, rec(l, i) + rec(i, r))
    dp[l][r] = res
    return res
print(rec(0, n))
