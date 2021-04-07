S = input()
s_n = len(S)
K = 'atcoder'
k_n = len(K)

# dp[i][j]: Sのi文字目までで部分文字列(Kのj文字目まで)を取り出せる通りの数
dp = [[0] * (k_n + 1) for i in range(s_n + 1)]
dp[0][0] = 1

for i in range(s_n):
    for j in range(k_n + 1): # k_n + 1にするの忘れない
        # S[i]を選択しない
        dp[i + 1][j] += dp[i][j]
        # S[i]を選択する
        if j < k_n and S[i] == K[j]:
            dp[i + 1][j + 1] += dp[i][j]

print(dp[s_n][k_n])
