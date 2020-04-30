# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_d
n = int(input())
l = list(map(int, input().split()))

dp = [[0] * 100 for _ in range(n + 1)]
# 最初の１個が入った状態でスタート
dp[1][l[0]] = 1
# 一つ目飛ばして二つ目からループさせていく
for i in range(1,n):
    for j in range(21):
        if j - l[i] >= 0:
            # dp[i + 1][j]に合流させていく
            dp[i + 1][j] += dp[i][j - l[i]]
        if j + l[i - 1] <= 20:
            dp[i + 1][j] += dp[i][j + l[i]]
print(dp[n - 1][l[-1]])
