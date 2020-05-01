# https://atcoder.jp/contests/joi2015yo/tasks/joi2015yo_d
n, m = map(int, input().split())
# 都市iに到達するためにdiかかる
# 都市0には最初から到達しているので先頭に0入れる
listd = [0]
for i in range(n):
    d = int(input())
    listd.append(d)
listc = []
for i in range(m):
    c = int(input())
    listc.append(c)

dp = [[float('inf')] * (m + 1) for i in range(n + 1)]
dp[0] = [0] * (m + 1)
# 移動する場合（iとjを１進める)と待機する場合（iを１進める）場合とでdpを比べる
# nが都市数 mが日にち
# iが現在の都市 jが現在の日にち
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # listd[i](都市i - 1→iに移動する) * listc[j - 1]（j - 1日目に都市i - 1を出発して
        # j日目に都市iに到達する
        dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1] + listd[i] * listc[j - 1])
print(dp[n][m])
