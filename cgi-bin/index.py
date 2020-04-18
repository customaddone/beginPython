def rec_memo(i, j):
    if dp[i][j]:
        return dp[i][j]
    if i == n:
        res = 0
    elif j < w[i]:
        res = rec_memo(i + 1, j)
    else:
        res = max(rec_memo(i + 1, j), rec_memo(i + 1, j - w[i]) + v[i])
    dp[i][j] = res
    return res

n = 4
w = [2, 1, 3, 2]
v = [3, 2, 4, 2]

W = 5
dp = [[0] * (W + 1) for i in range(n + 1)]  # メモ化テーブル
print(rec_memo(0, W))
