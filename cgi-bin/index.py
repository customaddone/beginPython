def rec(i, j):
    if dp[i][j]:
        return dp[i][j]
    if i == n:
        res = 0
    elif j < w[i]:
        res = rec(i + 1, j)
    else:
        res = max(rec(i + 1, j), rec(i + 1, j - w[i]) + v[i])

    dp[i][j] = res
    return res

n = int(input())
w = []
v = []
for i in range(n):
    w_, v_ = map(int, input().split())
    w.append(w_)
    v.append(v_)
W = int(input())

# 一つ多く枠をとる
dp = [[0] * (W + 1) for i in range(n + 1)]  # メモ化テーブル

print(rec_memo(0, W))
