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
mod = 10 ** 9 + 7

#############
# Main Code #
#############

class Multiset:
    def __init__(self):
        self.h = []
        self.d = dict()

    def insert(self,x):
        heappush(self.h,x)
        if x not in self.d:
            self.d[x] = 1
        else:
            self.d[x] += 1

    def erase(self,x):
        if x not in self.d or self.d[x] == 0:
            return 'not found'
        else:
            self.d[x] -= 1

        while len(self.h) != 0:
            if self.d[self.h[0]] == 0:
                heappop(self.h)
            else:
                break

    def erase_all(self,x):
        if x not in self.d or self.d[x] == 0:
            return 'not found'
        else:
            self.d[x] = 0

        while len(self.h) != 0:
            if self.d[self.h[0]] == 0:
                heappop(self.h)
            else:
                break

    def is_exist(self,x):
        if x in self.d and self.d[x] != 0:
            return True
        else:
            return False

    def get_min(self):
        if len(self.h) == 0:
            return 'enpty'
        return self.h[0]


N, Q = getNM()
limit = 2 * (10 ** 5) + 1

infants = [getList() for i in range(N)]
trans = [getList() for i in range(Q)]
belong = [0] * N
rate = [0] * N

school = [Multiset() for i in range(limit)]
purity = Multiset()

# 各学校にいる生徒を記録する
for i in range(N):
    a, b = infants[i]
    b -= 1
    belong[i] = b
    rate[i] = -a
    school[b].insert(-a)

# 各学校の最強園児を求める
for i in range(limit):
    if len(school[i].d) > 0:
        purity.insert(-school[i].get_min())

# 転園させる
for c, d in trans:
    c -= 1
    d -= 1
    ### 転園前処理 ###
    prev = belong[c] # 所属変更
    purity.erase(-1 * school[prev].get_min()) # 最強リストから削除
    school[prev].erase(rate[c]) # 前の学校から削除
    if len(school[prev].h) > 0:
        purity.insert(-1 * school[prev].get_min()) # 最強リストを更新
    ################

    ### 転園後処理 ###
    belong[c] = d
    after = belong[c] # 所属変更
    if len(school[after].h) > 0:
        purity.erase(-1 * school[after].get_min()) # 最強リストから削除
    school[after].insert(rate[c]) # 次の学校に追加
    purity.insert(-1 * school[after].get_min()) # 最強リストを更新
    #################

    print(purity.get_min())

# PAST3 L - スーパーマーケット
# 配列ver
class Multiset:
    def __init__(self):
        # x: [value, index]
        self.h = [] # 配列を入れる
        self.d = dict() # 値を入れる

    def insert(self, x):
        heappush(self.h, x)
        if x[0] not in self.d:
            self.d[x[0]] = 1
        else:
            self.d[x[0]] += 1

    def erase(self, x): # x: [value, index]で
        if x[0] not in self.d or self.d[x[0]] == 0:
            return 'not found'
        else:
            self.d[x[0]] -= 1

        while len(self.h) != 0:
            if self.d[self.h[0][0]] == 0:
                heappop(self.h)
            else:
                break

    def erase_all(self,x):
        if x[0] not in self.d or self.d[x[0]] == 0:
            return 'not found'
        else:
            self.d[x[0]] = 0

        while len(self.h) != 0:
            if self.d[self.h[0][0]] == 0:
                heappop(self.h)
            else:
                break

    def is_exist(self,x): # x: [value, index]で
        if x[0] in self.d and self.d[x[0]] != 0:
            return True
        else:
            return False

    def get_min(self):
        if len(self.h) == 0:
            return 'enpty'
        return self.h[0]

N = getN()
K = [deque(getList()[1:]) for i in range(N)] # 商品の棚
M = getN()
A = getList() # 客 全ての列についてAi番目まで見て値の大きいものを選ぶ
# それぞれの客について購入した商品の値を求める

"""
ヒープキュー？　aが小さいのでdequeでできる
列が一個しかない場合は？
1 ~ iのうち最大　をどのように求める？
一個取る　一個appendする
セグ木をK個立てるの無理なので、最大値をholdする
aが1か2
1 1の時
取る、取る
1 2の時
取る、（取る + 見る）
2 1の時
（取る + 見る）、見る
１番目の商品についてヒープキュー + ２番目の商品についてヒープキュー

1番目のものを取った　
2番目のものを1番目にappendする
2番目のものについてどう処理する

firについてheappop
Kについてpopleft

2つ目取ったらpop pop appendleft

multiset2つとis_number2があればOK
できる
"""

S1, S2 = Multiset(), Multiset()
# 番兵
for i in range(N):
    K[i].append(-mod)
# 2番目の数字は？
is_number2 = {}
for i in range(N):
    s1 = -K[i].popleft()
    # is_number1[i] = s1
    S1.insert([s1, i])

    if K[i]:
        s2 = -K[i].popleft()
        is_number2[i] = s2
        S2.insert([s2, i])

def pop_first():
    r1, index = S1.get_min()
    print(-r1)
    # S1から値を消す
    S1.erase([r1, index])
    # S2のものをS1に移動させる
    # S1にfloat('inf')が滞留するけど選ばないのでOK
    S1.insert([is_number2[index], index])
    S2.erase([is_number2[index], index])
    # S2に数字を入れる
    if K[index]:
        r2 = K[index].popleft()
        S2.insert([-r2, index])
        is_number2[index] = -r2

def pop_second():
    r2, index = S2.get_min()
    print(-r2)
    # S2の値を消す
    S2.erase([r2, index])
    # S2に数字を入れる
    # !K[index]だとis_numberにfloat('inf')が滞留するけど選ばないのでOK
    if K[index]:
        r2 = K[index].popleft()
        S2.insert([-r2, index])
        is_number2[index] = -r2

for i in A:
    if i == 1:
        # 値をprint
        pop_first()
    else:
        # -opt1の方が値が大きかったら
        if S1.get_min()[0] < S2.get_min()[0]:
            pop_first()
        else:
            pop_second()
