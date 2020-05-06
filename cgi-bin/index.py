# N回ジャンケンする　K回前のては使えない
N, K = map(int, input().split())
# グーで勝てばR点 チョキS パーP
RSP = list(map(int, input().split()))
# dpを使う
# 筺体が出す手
t = input()
# dp[i][j]: i回目にjを出した時の最大点数
dp = [[0] * 3 for i in range(N )]
# ジャンケンの手を変換する
def onetwothr(str):
    if str == "r":
        return 0
    elif str == "s":
        return 1
    else:
        return 2
# ジャンケンのジャッジをする
def judge(me, enemy):
    judgeint = [0, 1, 2]
    if judgeint[enemy - me] == 1:
        return RSP[me]
    else:
        return 0

print(judge(onetwothr('p'), onetwothr('s')))
