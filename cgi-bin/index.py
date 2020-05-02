# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_B&lang=ja
# https://qiita.com/mucunwuxian/items/10cb0f014964446fa2a3
# スカラー　独立した1つの数値 1, 11
# ベクトル　要素を一列に並べたもの [1, 2, 3, 4, 5]
# 行列  数字・文字を長方形や正方形に並べたもの [[1, 2, 3], [4, 5, 6]]
# a = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]の転置は
# at = [[2, 3, 4, 5, 6], [1, 2, 3, 4, 5]]
# 行が先、列が後
# [a, b], [c, d]のスカラー乗算の回数は
# [a, b] * [c, d]なら(a * d) * min(b, c) できるのはa * dの配列
# [c, d] * [a, b]なら(c * b) * min(d, a)　できるのはc * bの配列
# ヨコ([0][0])とタテ([1][1])を見る
import itertools
n = int(input())
lista = [list(map(int, input().split())) for i in range(n)]

dp = [[float('inf')] * n for i in range(n)]
for i in range(n):
    dp[i][i] = 0
    if i != n - 1:
        dp[i][i + 1] = lista[i][0] * lista[i + 1][0] * lista[i + 1][1]

def rec(r, c):
    minint = float('inf')
    # 区切りとなるkをr ~ c - 1の範囲で定める
    # (1)(2345)
    # (12)(345)
    # (123)(45) ((123)で最良の区分けをした)((45)で最良の区分けをした)
    # (1234)(5)
    for k in range(r, c):
        # 例えばk = 3なら
        # minint = min(minint, (123)で最良の区分けをした)通り　+ (45)で最良の区分けをした)通り
        # + (123)の行列の行 * (45)の行列の行(lista[k + 1]の行) * (45)の行列の列))
        minint = min(minint, dp[r][k] + dp[k + 1][c] + lista[r][0] * lista[k + 1][0] * lista[c][1])
    return minint
# [0][2], [1][3], [2][4], [3][5], [0][3]...
for i in range(2, n):
    for j in range(0, n - i):
        dp[j][j + i] = rec(j, j + i)
print(dp)
