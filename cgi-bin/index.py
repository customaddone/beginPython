from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right

import sys

def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getListGraph():
    return list(map(lambda x:int(x) - 1, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
inf = float('inf')
eps = 10 ** (-15)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

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

# Edufo 104 Cheap Dinner

"""
4種類から料理を選ぶ
i+1番目の料理がjの時の最小値

i+1番目の料理にjを選ぶ　この時i番目の料理として得られるのはmにないやつ
mの数は多くない　合計でもm
使えないものを消す　そのあと戻す
"""

N = getList()
D = [getList() for i in range(4)]
ma = max(N)
F = [[[] for i in range(ma)] for i in range(3)]
for i in range(3):
    n = getN()
    for _ in range(n):
        x, y = getNM()
        F[i][y - 1].append(x - 1)

prev = D[0] # 最初の料理

for i in range(3):
    next = [inf] * len(D[i + 1])
    # 相手になるi番目の料理　まずは全部追加
    q = Multiset()
    for v in prev:
        q.insert(v)

    # i+1番目の料理をjにした場合を求める
    for j in range(len(D[i + 1])):
        # 選べないものは除外する
        for k in F[i][j]:
            q.erase(prev[k])
        next[j] = min(next[j], q.get_min() + D[i + 1][j])
        # 戻す
        for k in F[i][j]:
            q.insert(prev[k])

    prev = next

if min(prev) == inf:
    print(-1)
else:
    print(min(prev))

# E. Rescheduling the Exam

"""
0とd+1を追加する
これがない場合の値をlogNぐらいで求められるか
一つ後ろのが増強される　あとは変わらず

一個とってどこかに置く
1引いて//2 もしくは一番後ろ　一番後ろに置く場合は定数
二分探索するか　~して条件を満たさないのが1個未満　かつ空きスペースがある
自身がなくなった場合
"""

T = getN()
for _ in range(T):
    t = input()
    N, D = getNM()
    A = [0] + getList()
    mi, ma = Multiset(), Multiset()

    for i in range(1, N + 1):
        l = A[i] - A[i - 1] - 1
        mi.insert(l)
        ma.insert(-l)

    # 一個手前まで
    ans = 0
    for i in range(1, N):
        be, af = A[i] - A[i - 1] - 1, A[i + 1] - A[i] - 1
        uni = A[i + 1] - A[i - 1] - 1
        # 自身を消す
        mi.erase(be)
        mi.erase(af)
        mi.insert(uni)
        ma.erase(-be)
        ma.erase(-af)
        ma.insert(-uni)
        ans = max(ans, min(mi.get_min(), max((-ma.get_min() - 1) // 2, D - A[-1] - 1)))
        mi.insert(be)
        mi.insert(af)
        mi.erase(uni)
        ma.insert(-be)
        ma.insert(-af)
        ma.erase(-uni)

    # 一番後ろ
    be = A[-1] - A[-2] - 1
    mi.erase(be)
    ma.erase(-be)
    ans = max(ans, min(mi.get_min(), max((-ma.get_min() - 1) // 2, D - A[-2] - 1)))
    print(ans)
