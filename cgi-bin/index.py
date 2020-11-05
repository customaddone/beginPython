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

# ABC030 D - へんてこ辞書

N, A = getNM()
K = getN()
B = getList()
A -= 1
B = [i - 1 for i in B]

visited = [-1] * N
visited[A] = 1

cnt = 1
to = B[A]

while cnt < K:
    cnt += 1
    if visited[to] >= 0:
        cnt += ((K - cnt) // (cnt - visited[to])) * (cnt - visited[to])
        visited = [-1] * N
    visited[to] = cnt
    to = B[to]

print(to + 1)

# ABC138 E - Strings of Impurity

s = input()
t = input()

# 各文字について
p = {c: [] for c in s}
for i in range(len(s)):
    p[s[i]].append(i)

z = 0
l = -1
for c in t:
    if c not in p:
        print(-1)
        break
    # 文字cのうちもっとも近い未来にあるもの
    x = bisect_right(p[c], l)
    # 一周するなら
    if x == len(p[c]):
        x = 0
        z += 1
    l = p[c][x]
else:
    print(z * len(s) + l + 1)

# ABC167 D - Teleporter

n, k = getList()
# dist
nums = [0] + getList()
cnt = 1
if k == 1:
    print(1)
    exit()
cur = 1
visited = [-1 for i in range(n + 1)]
visited[1] = 1
rooped = False
while True:
    # cur 行き先
    cur = nums[cur]
    cnt += 1

    # １回目に訪れていたら
    if visited[cur] != -1:
        # ループの周期
        roop = cnt - visited[cur]
        # 途中を飛ばす
        k -= ((k-cnt) // roop) * roop
        rooped = True
    if not rooped:
        # １回目に訪れたのであれば
        visited[cur] = cnt

    if cnt == k:
        print(nums[cur])
        break

# ABC175 D - Moving Piece

N, K = getNM()
P = [i - 1 for i in getList()]
C = getList()

ignore = [-1] * N
ans = -float('inf')
for i in range(N):
    if ignore[i] >= 0:
        continue
    ### ループ生成 ###
    ignore[i] = 1
    opt_l = [i]
    to = P[i]
    while ignore[to] == -1:
        opt_l.append(to)
        ignore[to] = 1
        to = P[to]
    ###
    ### 作成したループで得点リスト生成 ###
    n = len(opt_l)
    point = [0] * n
    for i in range(n):
        point[i] = C[opt_l[i]]
    ###
    ### 得点リスト内の連続する区間の総和のうちの最大値を累積和を使って求める ###
    sum_roop = sum(point)
    # ループの累積和作成
    imos = [0]
    point += point
    for i in range(len(point)):
        imos.append(imos[i] + point[i])
    #
    ran = min(n, K)
    for i in range(n):
        # 区間の大きさran以下についての総和を求める
        for j in range(1, ran + 1):
            if sum_roop >= 0:
                opt = imos[i + j] - imos[i] + ((K - j) // n) * sum_roop
            else:
                opt = imos[i + j] - imos[i]
            ans = max(ans, opt)
    ###
    
print(ans)

# AGC036 B - Do Not Duplicate

"""
長さN * K の数列Xがある
Xは数列AがK回続く

s = []
Xの全ての要素について
sがXiを含んでない場合append
sがXiを含んでいる場合末尾を削って削ってXiを取り除く

A内の要素についてもダブっている場合がある
Kは大きい <= 10 ** 12
X内の要素の個数について　順番は置いといて
A内に奇数個ある and Kが奇数 とは限らない　途中で削除に巻き込まれているかも

小さい例から試してみる
1 2 3 1 2 3の場合
２回目の1が出てくると前回の1が出る直前まで巻き戻り、2, 3だけが残る
1 2 3 1 2 3 1 2 3 の場合
2回目の3まで [2, 3]
3回目の1 [2, 3, 1]
3回目の2 全部削れる []
3回目の3 [3]

Kが大きいので一回の操作をO(1)で見つけても無理
法則性を見つける

・まず全ての要素が異なる場合
1 2 3
1番前の要素が真っ先に反応する　2, 3が残る
2番目の要素が反応する 3が残る
3番目の要素が反応する 何も残らない　最初に戻る

K % (N + 1)をする
1なら 1 2 3
2なら   2 3
3なら     3
4なら
5なら 1 2 3
6なら   2 3
7なら     3
8なら

同じ要素が出てきた場合
1 2 3 2 1 2 3 2 1 2 3 2
1周目
1周目2回目の2で2以下が全て削れる [1]

2周目
1が出る []
2周目2回目の2で全て削れる　[]

3周目
1周目と同じ [1]
どこかでループするんでは

同じものが出てきたら、その同じ要素 + 間のものが全て消える
Xiが偶数個しか出ないのであれば話は簡単
奇数個出る場合は？
シミュレーションすればいいのでは

3 1 4 1 5 9 2 6 5 3 5 の場合
先頭の3 次は2番目の3の次 5まで飛ぶ [5]
5は1番目の5の次9まで
9は1番目の9の次2まで　一周してる
飛んだ先がN - 1ならループ
ループを検出する　ループが検出できる
飛んだ先のindexを保存すればいいのでは

最大でも周期N + 1のループのはず
"""

N, K = getNM()
A = getList()
L = [[] for i in range(max(A) + 1)]
for i in range(N):
    L[A[i]].append(i)

roop = 1 # 現在のループ数
roop_index = [0] * (N + 1 + 1) # mod N回目はこのindex以降から始まる
now = 0

while now != N: # N - 1に飛ぶまで回す
    next_index = bisect_right(L[A[now]], now)
    if next_index == len(L[A[now]]): # roopが1進む
        roop += 1
        now = L[A[now]][0] + 1
    else: # 進まない
        now = L[A[now]][next_index] + 1

    roop_index[roop] = now

# ここからは実際にやってみよう
opt = A[roop_index[K % roop]:]
flag = [0] * (max(opt) + 1)

ans = []
for i in opt:
    if flag[i]:
        while flag[i]:
            u = ans.pop()
            flag[u] = 0
    else:
        ans.append(i)
        flag[i] = 1

print(*ans)



class Roop:
    def __init__(self, array):
        self.n = len(array)
        self.array = array
        # ループ検出
        self.roops = []
        # iはどのループのものか
        self.roop_dict = [-1] * self.n
        # ループ内の何番目にあるか
        self.opt_dic = [-1] * self.n
        ignore = [-1] * self.n
        cnt = 0
        for i in range(self.n):
            if ignore[i] >= 0:
                continue
            opt = [i]
            # opt内の何番目にあるか
            self.opt_dic[i] = 0
            c = 1
            # 探索したらフラグを立てる
            ignore[i] = cnt
            # i → array[i]
            to = array[i]
            # ループが詰まるまで回す
            while True:
                if ignore[to] == cnt:
                    # 作成してないならループ作成
                    for j in range(self.opt_dic[to], len(opt)):
                        self.roop_dict[opt[j]] = cnt
                    self.roops.append(opt[self.opt_dic[to]:])
                    # 次のループはcnt + 1番
                    cnt += 1
                    break
                opt.append(to)
                ignore[to] = cnt
                self.opt_dic[to] = c
                c += 1
                to = array[to]

    # xがどの番号のループにあるか
    def roop_n(self, x):
        return self.roop_dict[x]

    # xが入っているループは何か
    # ループ内になければFalse
    def inspect(self, x):
        if self.roop_n(x) == -1:
            return False
        return self.roops[self.roop_dict(x)]

    # ループの大きさ
    def roop_len(self, x):
        return len(self.roops[self.roop_n(x)])

    # xからk回移動してどの場所に行けるか
    def move(self, x, k):
        cnt = k
        to = x
        # ループに入る前にどのルートを通ったか
        # スタート地点から既にループに入っていた場合、headは空になる
        head = []
        # ループ脱出後どのルートを通るか
        tail = []
        # 何回ループしたか
        time = -1
        res = 0
        while cnt > 0:
            to = self.array[to]
            cnt -= 1
            # まだループしておらず、踏んだ場所がループ内にある場合
            if time == -1 and self.roop_n(to) >= 0:
                r = self.roops[self.roop_n(to)]
                time = (cnt // len(r))
                cnt -= time * len(r)
            # ループ前なら
            if time == -1:
                head.append(to)
            # ループ後なら
            else:
                tail.append(to)
        # 例: N, K = 6 727202214173249351
        # A = [6, 5, 2, 5, 3, 2]の時
        # 1回目の移動 1 → 6
        # 2回目の移動 6 → ### ここからループが始まる ### → 2
        # ... 242400738057749783回ループ
        # 727202214173249351回目の移動 3 → 2
        # to, head, tail, time = (1, [5], [1], 242400738057749783)
        return to

N, A = getNM()
A -= 1
K = getN()
B = [i - 1 for i in getList()]
roop = Roop(B)
print(roop.move(A, K) + 1)



# ABC167 D - Teleporter
N, K = getNM()
N -= 1
A = [i - 1 for i in getList()]
roop = Roop(A)
print(roop.move(0, K) + 1)



# ABC175 D - Moving Piece
N, K = getNM()
P = [i - 1 for i in getList()]
C = getList()
# ループ検出
roop = Roop(P)

# 各ループごと調べる
ans = -float('inf')
for r in roop.roops:
    n = len(r)
    # ループに対応するスコアリストを用意
    alta = []
    for i in range(n):
        alta.append(C[r[i]])
    # １回ループすると何点getできるか
    one_roop = sum(alta)
    alta += alta
    imos = [0]
    for i in range(len(alta)):
        imos.append(imos[i] + alta[i])

    t = min(n, K)
    for i in range(n):
        # 長さ1からtまでの区間の総和の最大値を探索
        for j in range(1, t + 1):
            if one_roop >= 0:
                opt = (imos[i + j] - imos[i]) + ((K - j) // n) * one_roop
            else:
                opt = imos[i + j] - imos[i]
            ans = max(ans, opt)

print(ans)
