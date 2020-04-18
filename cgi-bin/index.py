n,w = map(int,input().split())

#d[i][j]:i→jへの距離
d = [[float("inf")]*n for i in range(n)]
for i in range(w):
   x,y,z = map(int,input().split())
   d[x][y] = z

dp = [[-1] * n for i in range(1 << n)]

def rec(s, v, dp):
    if dp[s][v] >= 0:
        return dp[s][v]
    if s == (1 << n) - 1 and v == 0:
        dp[s][v] = 0
        return 0
    res = float('inf')
    for u in range(n):
        if (s >> u & 1) == 0:
            res = min(res,rec(s|(1 << u), u, dp) + d[v][u])
    dp[s][v] = res
    return res
print(rec(0,0,dp))
