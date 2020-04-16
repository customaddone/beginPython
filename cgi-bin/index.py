n,w = map(int,input().split())

#d[i][j]:i→jへの距離
d = [[float("inf")]*n for i in range(n)]
for i in range(w):
   x,y,z = map(int,input().split())
   d[x][y] = z

#     今いる点                 訪れた集合0b10110...
dp = [[-1] * n for i in range(1<<n)]


#訪れた集合がs、今いる点がvの時０に戻る最短経路
def rec(s,v,dp):
    if dp[s][v] >= 0:
        return dp[s][v]

    # 0b1000000 - 1 = 0b111111
    if s == (1<<n)-1 and v == 0:
        #全ての頂点を訪れた(s = 11...11 and v = 0)
        #最短距離0
        dp[s][v] = 0
        return 0

    res = float("inf")
    for u in range(n):
        #sをu右にずらした時の1桁目
        if (s>>u&1) == 0:
            #uに訪れていない時(uの箇所が0の時),次はuとすると
            #             uの箇所を1にして訪れた状態にしてrec
            res = min(res,rec(s|(1<<u),u,dp)+d[v][u])

    dp[s][v] = res
    return res
print(rec(0,0,dp))
