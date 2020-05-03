# https://atcoder.jp/contests/s8pc-1/tasks/s8pc_1_g
n,m= map(int, input().split())

INF=10**20
# g＝隣接行列
g=[[(INF,-1) for i in range(n)] for i in range(n)]

for i in range(m):
    s,t,d,u = map(int,input().split())
    g[s - 1][t - 1] = g[t - 1][s - 1] = (d,u)


# dp[S][v][0]: 訪れた点の集合がS。現在vにいてそこから帰ってくるときの最小距離。
# dp[S][v][1]:何通りあるか
dp=[[[INF, 1] for i in range(n)] for i in range(1 << n)]
dp[(1 << n) - 1][0]=[0, 1]


for s in range((1 << n) - 2, -1, -1):
    for j in range(n):
        for k in range(n):
            #Sがkを含んでいない時
            if not (s >> k) & 1:
                # 関門に間に合っているか
                if dp[s | 1 << k][k][0] + g[j][k][0] <= g[j][k][1]:
                    # 値が小さくなるなら更新。
                    if dp[s][j][0] > dp[s | 1 << k][k][0] + g[j][k][0]:
                        dp[s][j][0] = dp[s | 1 << k][k][0] + g[j][k][0]
                        dp[s][j][1] = dp[s | 1 << k][k][1]
                    # 値が同値なら、組み合わせに足す
                    elif dp[s][j][0] == dp[s | 1 << k][k][0] + g[j][k][0]:
                        dp[s][j][1] += dp[s | 1 << k][k][1]

if dp[0][0][0] < 10 ** 20:
    print(*dp[0][0])
else:
    print("IMPOSSIBLE")
