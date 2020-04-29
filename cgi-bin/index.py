# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C&lang=ja
# 個数制限あり重複ありナップサック
n, w = map(int, input().split())
val = []
wei = []
for i in range(n):
    v1, w1 = map(int, input().split())
    val.append(v1)
    wei.append(w1)
dp = [[0] * (w + 1) for i in range(n + 1)]
def rec_memo(i, j):
    if dp[i][j]:
        return dp[i][j]
    if i == n:
        res = 0
    else:
        res = rec_memo(i + 1, j)
        for r in range(n):
            # ここ「以下」になることに気をつける
            if wei[r] <= j:
                res = max(res, rec_memo(i + 1, j - wei[r]) + val[r])
    dp[i][j] = max(dp[i][j], res)
    return res
print(rec_memo(0, w))
