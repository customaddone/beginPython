from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import sys
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from bisect import bisect_left, bisect_right

def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

"""
mod mで考える
お気に入りがない場合
((ai+1 + m) - ai) % m回押す
お気に入りがある場合は上記の他に一発でmにする方法がある
mは意外と小さいぞ

((ai+1 + m) - ai) % m or ((ai+1 + m) - x) % m + 1
xの値を自由に決めてこれを最小化せよ
ai <= ai+1の時
ai+1 - ai
ai > ai+1の時
ai+1 + m - ai
xの値を決めた時に、お気に入りを使わない場合と比べてどれだけ軽減できるか考える
BITでできそうだけど
x <= ai+1の時
ai+1 - x + 1回
x > ai+1の時
ai+1 + m - x + 1
つまり aiとai+1、xとai+1の大小関係について計4通りを考える
ai <= ai+1, x <= ai+1の時
(x - 1) - ai分軽減できる
ai + 1 <= xなら軽減できる　（下回った値の個数) * (x - 1) - 下回った値の合計分減らせる

ai <= ai+1, x > ai+1
(ai+1 - ai) - (ai+1 + m - x + 1)
x - m - 1 - ai分軽減

ai > ai+1, x <= ai+1
(ai+1 + m - ai) - (ai+1 - x + 1)
(x - 1) + m - ai回

ai > ai+1,　x > ai+1
(ai+1 + m - ai) - (ai+1 + m - x + 1)
(x - 1) - ai回

・x - 1 - ai (ai <= ai+1, x <= ai+1)
・x - m - 1 - ai (ai <= ai+1, x > ai+1)
・x + m - 1 - ai (ai > ai+1, x <= ai+1)
・x - 1 - ai (ai > ai+1,　x > ai+1)
これらは全て独立ですが ai+1の値が関係なくなるので

4 6
1 5 1 4
[1, 0, 1] <=
[0, 5, 0] >

BITを4本持とう
aiの値を保持する ai+1を基準に変更していく
xの数を順に増やしていって、ai+1が同じになったところから消していく
x = 1
[1, 0, 1]
[0, 0, 0]
[0, 5, 0]
[0, 0, 0]
x = 2
[1, 0, 1]
[0, 0, 0]
[0, 0, 0]
[0, 5, 0] 上のとスイッチした
x = 4
[1, 0, 1] 4 - 1 - 1 = 2を二回 4軽減できる
[0, 0, 0]
[0, 0, 0]
[0, 5, 0] 4 - 1 - 5 = -2できるがやる必要はない

待機してもらう
"""

N, M = getNM()
A = getList()

cnt = [0] * 4 # 個数を数える
value = [0] * 4 # 合計の値
que = [[] for i in range(4)] # 待機
bef = [A[i] for i in range(N - 1)]
aft = [[A[i + 1], i, 0] for i in range(N - 1)]

for i in range(N - 1):
    if bef[i] <= aft[i][0]:
        heappush(que[0], bef[i])
    else:
        heappush(que[2], bef[i])
        aft[i][2] = 1 # 印をつける

aft.sort(reverse = True)
for m in range(1, M + 1):
    while aft and aft[-1][0] < m:
        _, index, dir = aft.pop()
        if dir == 0:
            que1[index], que2[index] = que2[index], que1[index]
        else:
            que3[index], que4[index] = que4[index], que3[index]
