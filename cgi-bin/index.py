n = 5
a = [7, 5, 1, 3, 8]
A = 12

def dfs(a, A):
    p = 10 ** 9 + 7
    N = len(a)
    # 一旦float('inf')に
    dp = [[float('inf')] * (A + 1) for i in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(A + 1):
            if a[i] <= j:
                dp[i + 1][j] = min(dp[i][j - a[i]] + 1, dp[i][j])
            else:
                dp[i + 1][j] = dp[i][j]
    return dp[N][A]
print(dfs(a, A))
