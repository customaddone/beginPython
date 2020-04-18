s = 'pirikapirirara'
t = 'poporinapeperuto'

def dfs(s, ts):
    lens = len(s)
    lent = len(t)
    dp = [[0] * (lent + 1) for i in range(lens + 1)]
    dp[0][0] = 0

    for i in range(lens):
        for j in range(lent):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = max(dp[i][j] + 1, dp[i + 1][j], dp[i][j + 1])
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[lens][lent]
print(dfs(s, t))
