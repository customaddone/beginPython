w = [2, 1, 3, 2, 1, 5]
v = [3, 2, 6, 1, 3, 85]
n = 6
W = 9
def rec_memo(i, j):
    if dp[i][j]:
        return dp[i][j]
    if i == n:
        return 0
    elif j < w[i]:
        res = rec_memo(i + 1, j)
    else:
        res = max(rec_memo(i + 1, j), rec_memo(i + 1, j - w[i]) + v[i])
    dp[i][j] = res
    return res
# iが先 jが後
dp = [[0] * (W + 1) for i in range(n + 1)]
print(rec_memo(0, W))
