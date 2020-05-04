# https://www.ioi-jp.org/joi/2009/2010-ho-prob_and_sol/2010-ho.pdf#page=2
# MLE対策
import sys
def input(): return sys.stdin.readline()[:-1]

# mが縦, nが横
M, N = map(int, input().split())
K = int(input())
planet = []
for i in range(M):
    j = input()
    planet.append(list(j))
prove = []
for i in range(K):
    p = list(map(int, input().split()))
    prove.append(p)

# 二次元累積和
dpJ = [[0] * N for i in range(M)]
dpO = [[0] * N for i in range(M)]
dpI = [[0] * N for i in range(M)]

# dpを整理する関数
def planet_counter(str, dp):
    # まず横の累積和
    for i in range(M):
        if planet[i][0] == str:
            dp[i][0] = 1
        for j in range(1, N):
            if planet[i][j] == str:
                dp[i][j] = dp[i][j - 1] + 1
            else:
                dp[i][j] = dp[i][j - 1]
    # 次に縦の累積和
    for i in range(1, M):
        for j in range(N):
            dp[i][j] += dp[i - 1][j]
# 実行
planet_counter("J", dpJ)
planet_counter("O", dpO)
planet_counter("I", dpI)

# 集計する関数
def planet_square(arr, dp):
    mother = 0
    west = 0
    north = 0
    northwest = 0
    if arr[0] - 1 > 0 and arr[1] - 1 > 0:
        northwest = dp[arr[0] - 2][arr[1] - 2]
    if arr[0] - 1 > 0:
        north = dp[arr[0] - 2][arr[3] - 1]
    if arr[1] - 1 > 0:
        west = dp[arr[2] - 1][arr[1] - 2]
    mother = dp[arr[2] - 1][arr[3] - 1]

    """
    12 12 2 2 2 2
    12 12 2 2 2 2
    1  1  3 3 3 3
    1  1  3 3 3 3
    1  1  3 3 3 3
    全体 - 1の部分 - 2の部分 + ダブったところ
    """
    return mother - west - north + northwest

ans = [[] for i in range(K)]
# 実行
for i in range(K):
    ans[i].append(planet_square(prove[i], dpJ))
    ans[i].append(planet_square(prove[i], dpO))
    ans[i].append(planet_square(prove[i], dpI))
for s in ans:
    print(*s)
