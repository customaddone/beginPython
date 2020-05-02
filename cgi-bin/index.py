# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_2_A&lang=ja
n,w = map(int,input().split())

#d[i][j]:i→jへの距離
d = [[float("inf")]*n for i in range(n)]
for i in range(w):
   x,y,z = map(int,input().split())
   d[x][y] = z

dp = [[-1] * n for i in range(1 << n)]

#訪れた集合がs、今いる点がvの時０に戻る最短経路
def rec(s, v, dp):
    if dp[s][v] >= 0:
        return dp[s][v]
     #全ての頂点を訪れた(s = 11...11 and v = 0)
    if s == (1 << n) - 1 and v == 0:
        dp[s][v] = 0
        return 0
    res = float('inf')
    for u in range(n):
        if (s >> u & 1) == 0:
            # 道が無い場合はfloat('inf')
            # v → u1, u2...と探していく
            res = min(res,rec(s|(1 << u), u, dp) + d[v][u])
    dp[s][v] = res
    return res
# 結局のところ0からスタートしようが1からスタートしようが同じ道を通る
print(rec(0,0,dp))
