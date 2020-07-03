def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

def knapsack_6(N, upper, weight, value):
    dp = [[[0] * (upper + 1) for i in range(2)] for j in range(N + 1)]

    for i in range(N):
        # ボーナスでコスト１にするのを使ったか
        for j in range(2):
            for l in range(upper + 1):
                if j == 0:
                    if l >= weight[i]:
                        dp[i + 1][j][l] = max(dp[i][j][l], dp[i][j][l - weight[i]] + value[i])
                        dp[i + 1][j + 1][l] = max(dp[i][j + 1][l], dp[i][j][l - 1] + value[i])
                    elif l >= 1:
                        dp[i + 1][j + 1][l] = max(dp[i][j + 1][l], dp[i][j][l - 1] + value[i])
                    else:
                        dp[i + 1][j][l] = dp[i][j][l]
                else:
                    if l >= weight[i]:
                        dp[i + 1][j][l] = max(dp[i + 1][j][l], dp[i][j][l - weight[i]] + value[i])
                    else:
                        dp[i + 1][j][l] = dp[i + 1][j][l]
    return dp[N][0]

print(knapsack_6(N, A, w, v))
