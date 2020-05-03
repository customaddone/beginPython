N, M = map(int, input().split())
inf = float('inf')

# 全ての街から、その他の街へ行く場合のコスト
g = [[(inf, -1) for i in range(N)] for i in range(N)]

for i in range(M):
    s, t, d, u = map(int, input().split())
    # 双方向なので
    g[s - 1][t - 1] = g[t - 1][s - 1] = (d, u)

# dp[S][v][0]: 訪れた点の集合がS。現在vにいて0地点に帰ってくるときの最小距離。
# dp[S][v][1]:何通りあるか
dp = [[[inf, 1] for _ in range(N)] for _ in range(1 << N)]

# 全てが1=到達済みの場合は 0地点へ帰るのはコスト0。
dp[(1 << N) - 1][0] = [0, 1]
# print(g)
# print(dp)

# 訪れた集合がs
# 今いる点がv
# 0に戻る最短経路を計算する

# 01110まではやる必要がある
# 01111はやる必要がないので(1 << N) - 2
for s in range((1 << N) - 2, -1, -1):
    # スタート地点はN個あるため。
    for j in range(N):

        for k in range(N):
            # Sがkを含んでいない時
            # すでに到達済みの集合に、次に進む点が入っていない
            if not (s >> k) & 1:
                # 過去のコスト+次のコストが時間内に終わっているか
                # s | 1 << kは、すでに到達済みの集合sと、1<<kの論理和をとる。
                # 10000 | 01111なら11111
                if dp[s | 1 << k][k][0] + g[j][k][0] <= g[j][k][1]:
                    # 値が小さくなるなら更新。
                    if dp[s][j][0] > dp[s | 1 << k][k][0] + g[j][k][0]:
                        dp[s][j][0] = dp[s | 1 << k][k][0] + g[j][k][0]
                        dp[s][j][1] = dp[s | 1 << k][k][1]
                    # 値が同値なら、組み合わせに足す
                    elif dp[s][j][0] == dp[s | 1 << k][k][0] + g[j][k][0]:
                        dp[s][j][1] += dp[s | 1 << k][k][1]

if dp[0][0][0] < inf:
    print(*dp[0][0])
else:
    print("IMPOSSIBLE")
