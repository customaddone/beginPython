# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d
# dpの三重ループ
n, k =map(int, input().split())
mod = 10000
day = [-1] * n
for i in range(k):
    a, b = map(int, input().split())
    day[a - 1] = b - 1
# dpは三重に
# 一重目:日にち
# 二重目:その日のパスタ
# 三重目:前日のパスタ
dp = [[[0] * 3 for i in range(3)] for j in range(n)]

# 既に1日目のパスタが決定されていたなら
if day[0] >= 0:
    # そのパスタを選択
    d = day[0]
    # １日目、パスタd、前日のパスタはパスタd以外という１通り
    dp[0][d][d - 1] = 1
# 決定されていなかったら
else:
    for i in range(3):
        # 全てのパスタについて一通りをプラス
        dp[0][i][i - 1] = 1
for i in range(1, n):
    # パスタが決定されているかいないか
    d = day[i]
    if day[i] >= 0:
        for j in range(3):
            for k in range(3):
                # もし３日とも同じなら
                if d == j and j == k:
                    continue
                # i日目、パスタd、前日のパスタjにi - 1日目、パスタj、前日のパスタkの通り
                # をプラス
                dp[i][d][j] += dp[i - 1][j][k]
                dp[i][d][j] %= mod
    else:
        # その日のパスタ
        for j in range(3):
            # 前日のパスタ
            for k in range(3):
                # 前々日のパスタ
                for l in range(3):
                    if j == k and k == l:
                        continue
                    dp[i][j][k] += dp[i - 1][k][l]
                    dp[i][j][k] %= mod
ans = 0
# dp[-1]の全ての通りを集計
for i in range(3):
    for j in range(3):
        ans += dp[-1][i][j]
        ans %= mod
print(ans)
