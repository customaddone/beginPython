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
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from collections import defaultdict, deque, Counter
from sys import exit
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 998244353

#############
# Main Code #
#############

# ABC005 C - おいしいたこ焼きの売り方
# マッチング問題だが貪欲
T = getN()
N = getN()
sell = getList()
M = getN()
buy = getList()

# 来る客1, 2に売れるか
for cus in buy:
    flag = False
    for i in range(N):
        if sell[i] <= cus <= sell[i] + T:
            flag = True
            sell[i] = mod
            break
    if not flag:
        print('no')
        exit()
print('yes')

# ABC080 D - Recording
# 使ってない録画機は他のチャンネルにスイッチできる
# 同時にいくつ放送が流れているか
N, C = getNM()
query = [getList() for i in range(N)]
dp = [[0] * (C + 1) for i in range(10 ** 5 + 2)]
for i in range(N):
    s, t, c = query[i]
    dp[s][c] += 1
    dp[t + 1][c] -= 1

for i in range(1, 10 ** 5 + 2):
    for j in range(C + 1):
        dp[i][j] += dp[i - 1][j]

ans = 0
for i in range(10 ** 5 + 2):
    cnt = 0
    for j in dp[i]:
        if j > 0:
            cnt += 1
    ans = max(ans, cnt)
print(ans)

# ABC085 D - Katana Thrower
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
# 実は投げてしまった刀も振ることができるというルールに変更しても
# 問題の答えは変わらない
# 実際のムーブとしては
# ①最も攻撃力が高い振り刀で攻撃する
# ②一定の体力以下になると攻撃力が高い順に投げ刀で攻撃していって撃破
# という流れになる
for x in reversed(sorted(filter(lambda x: x >= max_a, b))):
    H -= x
    ans += 1
    if H <= 0: break

ans += max(0, (H + max_a - 1) // max_a)
print(ans)

# ABC091 C - 2D Plane 2N Points

N = getN()
# Rはループさせるのでソートさせる必要ない
R = [getList() for i in range(N)]
R_l = [1] * N

B = [getList() for i in range(N)]
B.sort()

# 貪欲法でペア作りする問題
# ABC005 C - おいしいたこ焼きの売り方の時と同様に
# それとしか繋げないもの　を優先的に繋いでいく

# 条件Aの通過が厳しい順に対象bをソートし、
# たこ焼き　条件A:客が来る前にたこ焼きができてないといけない
#  　　　　      客を来るのが早い順に並べる（最初から並んでる）
# 今回     条件A:赤星のx座標が青星のx座標より小さくないといけない
#  　　　　　　　 青星をx座標が小さい順に並べる

# 条件A, 条件Bをクリアしたものの中で、最も条件Bの通過が厳しい対象aと結ぶ
# たこ焼き　条件B:たこ焼きが賞味期限より前のものでないといけない
#  　　　　      できるだけ古いものを売る（最初から並んでる）
# 今回     条件B:赤星のy座標が青星のy座標より小さくないといけない
#  　　　　　　　 条件をクリアしたもののうちでできるだけy座標が大きいものを選ぶ

ans = 0
for b in B:
    max_y = -1
    max_index = -1
    for i, a in enumerate(R):
        # x, y座標が小さいもののうちでまた使ってないもの
        if a[0] < b[0] and a[1] < b[1] and R_l[i] == 1:
            # あるならY座標が最も大きいもの
            if a[1] > max_y:
                max_y = a[1]
                max_index = i
    if max_y >= 0:
        R_l[max_index] = 0
        ans += 1

# ABC100 D - Patisserie ABC
# 8パターン全部調べる

N,M = getNM()
data = [[] for i in range(8)]
for _ in range(N):
    x,y,z = getNM()
    data[0].append(x + y + z)
    data[1].append(x + y - z)
    data[2].append(x - y + z)
    data[3].append(x - y - z)
    data[4].append(- x + y + z)
    data[5].append(- x + y - z)
    data[6].append(- x - y + z)
    data[7].append(- x - y - z)

ans = -mod
for i in range(8):
    data[i].sort(reverse = True)
    ans = max(ans,sum(data[i][:M]))
print(ans)

# ABC116 D - Various Sushi
N, K = getNM()
various = defaultdict(list)
que = [getList() for i in range(N)]

ans = 0
num = []
var_s = set()

# 美味しい順にK個とった時の幸福度
que.sort(reverse = True, key = lambda i: i[1])
for i in range(K):
    ans += que[i][1]
    # もし２番手以降ならあとで交換する用にとっておく
    if que[i][0] in var_s:
        num.append(que[i][1])
    var_s.add(que[i][0])

var = len(var_s)
ans += var ** 2

# 使ってない種類について各種類で一番大きさが大きいもの
left_l = defaultdict(int)
for i in range(N):
    if not que[i][0] in var_s:
        left_l[que[i][0]] = max(left_l[que[i][0]], que[i][1])

num.sort(reverse = True)
left_l = [i[1] for i in left_l.items()]
left_l.sort()

# M回交換する
opt = ans
M = min(len(num), len(left_l))
for i in range(M):
    u = num.pop()
    s = left_l.pop()
    # 寿司単体の幸福度
    opt -= (u - s)
    # 種類が増える分
    opt += 2 * var + 1
    var += 1
    ans = max(opt, ans)

print(ans)
