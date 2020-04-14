def part_sum(a, A):
    p = 10 ** 9 + 7
    N = len(a)
    dp = [[0] * (A + 1) for i in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(A + 1):
            if a[i] <= j:
                # 足したパターンと足さなかったパターンの合計
                dp[i + 1][j] = dp[i][j - a[i]] + dp[i][j]
            else:
                dp[i + 1][j] = dp[i][j]
    return dp[N][A]

a = [1, 3, 5, 7, 9]
A = 10
print(part_sum(a, A))
