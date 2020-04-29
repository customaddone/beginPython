# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C&lang=ja
# 個数制限あり重複ありナップサックdp
n, w = map(int, input().split())
val = []
wei = []
for i in range(n):
    v1, w1 = map(int, input().split())
    val.append(v1)
    wei.append(w1)
dp = [[0] * (w + 1) for i in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(w + 1):
        dp[i + 1][j] = dp[i][j]
        for r in range(n):
            if wei[r] <= j:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - wei[r]] + val[r])
print(dp[n][w])
