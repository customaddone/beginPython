s = 'pirikapirirara'
t = 'poporinapeperuto'

def dfs(s, t):
    lens = len(s)
    lent = len(t)
    dp = [[float('inf')] * (lent + 1) for i in range(lens + 1)]
    dp[0][0] = 0

    for i in range(lens):
        for j in range(lent):
            if s[i] == t[j]:
                # dp[i + 1][j + 1]はdp[i + 1][j]、dp[i][j + 1] と比べて削除、挿入の手間が１つ増える
                dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j] + 1, dp[i][j + 1] + 1)
            else:
                dp[i + 1][j + 1] = min(dp[i + 1][j] + 1, dp[i][j + 1] + 1)
    return dp[lens][lent]
print(dfs(s, t))
