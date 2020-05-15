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

from collections import defaultdict, deque, Counter
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

N, H = getNM()

a = []
b = []

for i in range(N):
  x, y = map(int, input().split())
  a.append(x)
  b.append(y)

# 振った場合の最大値
max_a = max(a)

ans = 0
# 振る刀の最大攻撃力より高い攻撃力を持つ投げ刀を高い順にソートする
# 刀iで好きなだけ振って攻撃する→気が済んだら投げることで振りの攻撃力と投げの攻撃力を
# 両方利用することができる
# 実は投げてしまった刀も振ることができるというルールに変更しても
# 問題の答えは変わらない
# 実際のムーブとしては
# ①最も攻撃力が高い振り刀で攻撃する
# ②一定の体力以下になると攻撃力が高い順に投げ刀で攻撃していって撃破
# という流れになる
for x in reversed(sorted(filter(lambda x: x >= max_a, b))):
    H -= x
    ans += 1
    if H <= 0: break

# max_aをN回繰り返してH以上にするコード
ans += max(0, (H + max_a - 1) // max_a)
print(ans)
