from collections import defaultdict, deque, Counter
import sys
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce, lru_cache
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

# ABC161 D - Lunlun Number
K = 13
que = []
heapify(que)
for i in range(1, 10):
    que.append(i)
for i in range(K):
    u = heappop(que)
    if u % 10 != 0:
        heappush(que, 10 * u + (u % 10) - 1)
    heappush(que, 10 * u + (u % 10))
    if u % 10 != 9:
        heappush(que, 10 * u + (u % 10) + 1)
print(u)

N, M = getNM()
weight = []
key = []
for _ in range(M):
    a, b = getNM()
    weight.append(a)
    c = getList()
    key.append(c)
dp = [float('inf')] * (1 << N)
dp[0] = 0
for i in range(M):
    bit = 0
    for item in key[i]:
        bit |= (1 << (item - 1))
    for j in range(1 << N):
        dp[j | bit] = min(dp[j | bit], dp[j] + weight[i])
print(dp)


# ARC028 B-特別賞

"""
N: 人数 K:　K番目に若い人
X1, X2... :　i位の人の年齢はXi
K番目の人を求めるのは大体ヒープキュー
K個ぶち込んでから　
①最大のものがK番目に大きい数字　これをprint
②一個入れる(K+1個になる)→最大のものを取り出す（K+1番目以降のものなのでいらない）　を繰り返す
"""

N, K = getNM()
X = getList()

# K個ぶち込んでから　
pos = [[-X[i], i] for i in range(K)]
heapify(pos)

# 出し入れ
for i in range(K, N):
    print(pos[0][1] + 1)
    heappush(pos, [-X[i], i])
    _ = heappop(pos)

print(pos[0][1] + 1)

# ABC062 D - 3N Numbers
N = getN()
A = getList()
# foreとbackの境界線を移動させる
# [3 1 4 1 5 9]の場合
# foreは[3 1], [3 1 4], [3, 1, 4, 1]の場合
# backは[5 9], [1 5 9], [4, 1, 5, 9]の場合を前計算
# 前から計算
fore = A[:N]
# 後ろから計算
back = A[2 * N:]
back = [-i for i in back]
for_sum = sum(fore)
back_sum = sum(back)
heapify(fore)
heapify(back)

fore_list = []
back_list = []
for i in range(N):
    fore_list.append(for_sum)
    back_list.append(back_sum)
    in_fore = A[N + i]
    heappush(fore, in_fore)
    out_fore = heappop(fore)
    for_sum += in_fore - out_fore

    in_back = (-1) * A[-N - i - 1]
    heappush(back, in_back)
    out_back = heappop(back)
    back_sum += in_back - out_back

fore_list.append(for_sum)
back_list.append(back_sum)

ans = -float('inf')
for i in range(N + 1):
    opt = fore_list[i] + back_list[N - i]
    ans = max(ans, opt)
print(ans)

# ABC123 D - Cake 123
X, Y, Z, K = getNM()
A = sorted([-i for i in getList()])
B = sorted([-i for i in getList()])
C = sorted([-i for i in getList()])
pos = []
heapify(pos)
dict = defaultdict(int)
u = (A[0] + B[0] + C[0], 0, 0, 0)
heappush(pos, u)
dict[u] = 1
for i in range(K):
    p, i, j, l = heappop(pos)
    print(-p)
    # 取り出すごとにA, B, Cについての次の値をpush
    if i + 1 < X:
        opt_a = (A[i + 1] + B[j] + C[l], i + 1, j, l)
        if dict[opt_a] == 0:
            heappush(pos, opt_a)
            dict[opt_a] = 1
    if j + 1 < Y:
        opt_b = (A[i] + B[j + 1] + C[l], i, j + 1, l)
        if dict[opt_b] == 0:
            heappush(pos, opt_b)
            dict[opt_b] = 1
    if l + 1 < Z:
        opt_c = (A[i] + B[j] + C[l + 1], i, j, l + 1)
        if dict[opt_c] == 0:
            heappush(pos, opt_c)
            dict[opt_c] = 1

# ABC137 D - Summer Vacation

N, M = getNM()
query = [getList() for i in range(N)]

A_list = [[] for i in range(10 ** 5 + 1)]
for a, b in query:
    A_list[a].append(b)

job = []
heapq.heapify(job)

ans = 0
for i in range(1, M + 1):
    for j in A_list[i]:
        heapq.heappush(job, -j)
    if len(job) > 0:
        u = heapq.heappop(job)
        ans += -u
print(ans)

# ABC149 E - Handshake
# Mがクソデカイので使用不可
# 二分探索使ってね
N, M = getNM()
A = sorted([-i for i in getList()])

pos = []
heapify(pos)
dict = defaultdict(int)
u = (A[0] + A[0], 0, 0)
heappush(pos, u)
dict[u] = 1

ans = 0
# 大きい値M番目まで全て求まる
for i in range(M):
    p, i, j = heappop(pos)
    ans += -p
    if i + 1 < N:
        opt_a = (A[i + 1] + A[j], i + 1, j)
        if dict[opt_a] == 0:
            heappush(pos, opt_a)
            dict[opt_a] = 1
    if j + 1 < N:
        opt_b = (A[i] + A[j + 1], i, j + 1)
        if dict[opt_b] == 0:
            heappush(pos, opt_b)
            dict[opt_b] = 1
print(ans)

# Code Formula 2014 予選A C - 決勝進出者

"""
N: 予選の回数
K: 招待人数
最高順位が高い順に　どこかの予選でハイスコアを出せばOK
最高順位が同じ場合は、最高順位を取った予選が開かれた時期が早い方から先に選ばれる。
現在の試合を含めた残り試合数 = dとすると
(K + d - 1) // dの人数分上から順番にとる
2 11
1 2 3 4 5 6 7 8 9 10 11
1 2 15 14 13 16 17 18 19 20 21

の場合
[[1, 2, 3, 4, 5, 6], [15, 14, 13]] ここまでいける
[1 2 3 4 5 6] 7 8 9 10 11
[1 2 15 14 13] 16 17 18 19 20 21
1番目の6位までと2番目以降の5位までは問答無用で確定する
後をどうするか
枠が空く　このまま順調に取っていっても枠が余る場合は
枠が空いた場合は再計算
N <= 50しかない
優先度何番目かをレコードする
枠が空くたびにボーダーが下がる

4 5
1 2 3 4 5
2 1 3 4 5
1 2 3 4 5
2 1 3 4 5 の場合

一番最初に2人通過できる？
制約が小さいので50回全探索できる

iを一つ進めるごとに候補がA[i]の分だけ増える
これをヒープキューで優先度が高い（数字が小さい）順に取る
"""

N, K = getNM()
A = [[] for i in range(N)]
for i in range(N):
    a = getList()
    for j in range(K):
        A[i].append([j * N + i + 1, a[j]])

ans = [[] for i in range(N)]
L = []
heapify(L)
passed = set()

for i in range(N):
    for j in A[i]:
        heappush(L, j)
    while L and L[0][0] <= K: # whileで抜き取る時は要素が残っているか気をつけよう
        pref, id = heappop(L)
        if id in passed:
            K += 1
        else:
            ans[i].append(id)
            passed.add(id)

for i in ans:
    print(*sorted(i))

# ARC098 E - Range Minimum Queries

"""
数列A
長さKの連続する部分列を1つ選ぶ　
その中の最小のものを取り除く　infにすれば？
取り除いた要素の最大値 - 最小値をマイナスにしたい　二分探索とかできる?
最終形をイメージする

一番望ましいのは
Q個について最小区間のQ個を取ること
それより小さい要素を取らずに都合のいいとこだけ取りたい
小さい順に仕切りを立てていく
まず小さい順に1 2 3 4...これは必ず取れる　（1 2 3 5...とかは1234より大きくなる）
次に2 3 4 5を取れるか
N個目の数って難しくない？

5 3 2
4 3 1 5 2 の場合
4 3 [1 5 2]
4 [3 5 2]

N <= 2000なので 1, 2, 3, 4で区切っていくのはできそう
Qの中に1を入れる場合、求める値はAq - A1

1 1 3 5 6 7 の場合
1番目の1以降を使うと 1 1 3 5
2番目の1以降を使うと 1 3 5 6
3以降を使うと       3 5 6 7
なので3以降を使う方がいい
Q = 4の時、候補となるのは
[小さい方から1番目、2番目、3番目...] or
[小さい方から2番目、3番目、4番目...] or...

ただし、[小さい方から2番目、3番目、4番目...]を作るには選択範囲に小さい方から1番目を含めないことが必要
4 3 1 5 2 の場合
　　 ×     1は障害物になる
ブロック1:[4, 3]
ブロック2:[5, 2] の中でしかKを回せない
[小さい方から3番目、4番目、5番目...]の場合
ブロック1:[4, 3]
ブロック2:[5]
"""

N, K, Q = getNM()
A = getList()
A = [[A[i], i] for i in range(N)]

flag = [0] * N
# 区切り0
l = deepcopy(sorted(A))
opt = []
l.sort()
for i in range(Q):
    opt.append(l[i][0])
ans = opt[-1] - opt[0]

# 区切り1個以上
for i in range(N):
    # indexの位置はlを再利用
    flag[l[i][1]] = 1 # A[i][1]はindex
    parent = []
    child = []
    # フラグの立っているところで区切る
    # 要素の探索はAを使う
    for j in range(N):
        if flag[j] == 0:
            child.append(A[j][0])
        else:
            child.sort()
            parent.append(child)
            child = []
    if len(child):
        child.sort()
        parent.append(child)

    # 値を求める
    # 各childから取れるだけ取る(配列操作を行う)
    opt = []
    for array in parent:
        for j in range(len(array) - K + 1): # childの長さ - K + 1だけ値を取れる
            opt.append(array[j])
    # Q個取れたなら
    if len(opt) >= Q:
        opt.sort()
        ans = min(ans, opt[Q - 1] - opt[0])

print(ans)

"""
前から処理すると、nxt以前で確定したものはもう見なくて済む
s, cを取る
if s + cがnxtより前で終了する
優先度に関わらず確定させて良い
else nxt以降に続く
あとでスタートする優先度がより高いものが関係するかもしれないので
nxt - s(次のスタート - 今のスタート)して順番待ちする
"""

N = getN()
Q = [getList() for i in range(N)]
# スタートが早い順にソート
Q = sorted([[Q[i][0], Q[i][1], i] for i in range(N)]) # クエリソート
Q.append([float('inf'), -1, -1])

ans = [0] * N
q = []

for i in range(N): # 前のやつから順に
    s, c, index = Q[i]
    # スタート地点は不変
    heappush(q, (index, c))
    nxt, _, _ = Q[i + 1] # nxt: 次のスタート地点

    while q: # 現在残っているqはまだ伸びるもの
        index, c = heappop(q) # 優先度が高い順に処理する
        if s + c - 1 < nxt: # 次のスタートまでは行かない
            ans[index] = s + c - 1 # 確定
            s += c # s ~ c間はカウントされないので次からはs + cからスタート
        else:
            c -= nxt - s # 次の奴まで突き刺さる
            heappush(q, (index, c)) # 戻す
            break # 優先度が高いものを処理し終わらないと次のができない

for res in ans:
    print(res)

# JOI 2018/2019 予選 過去問 E イルミネーション (Illumination)

"""
区間問題なのでセグ木か？
まずは貪欲な方法を考える

区間内は1つのみ
美しさの最大値: dpする？
区間をソートする
ぴょんぴょんするdpを考える
[[1, 3], [2, 4]]
1に置いた場合は次4以降にしか置けない
最後にiに置いた場合を考える
N <= 100000
iに置けますか？
iがかかるクエリを探索　一番厳しいものが制約になる
[0, 1, 2, 3, 4]
[0, 0, 0, 3, 4] [1, 3]のクエリについて
[0, 0, 0, 1, 4] [2, 4]のクエリについて
イベントソートっぽくすると
"""

N, M = getNM()
A = getList()
forbit = [getList() for i in range(M)]
forbit.sort(reverse = True)

l = [i - 1 for i in range(N + 1)]
# 範囲をheapqueで管理する
# 区間の問題をheapque使ってイベントソートっぽくするのはよくやる
# queryをするのが途中でない場合はセグ木使わなくていい
que = []
for i in range(1, N + 1):
    # いらないものを捨てる
    while que and que[0][1] < i:
        heappop(que)
    # 追加する
    while forbit and forbit[-1][0] == i:
        heappush(que, forbit.pop())
    # dpを書く
    if que:
        l[i] = que[0][0] - 1

# 累積和っぽく
ans = [0] * (N + 1) # iに置いた場合の最大値
ma = [0] * (N + 1) # i番目以前の最大値
for i in range(1, N + 1):
    ans[i] = ma[l[i]] + A[i - 1]
    ma[i] = max(ma[i - 1], ans[i])
print(max(ans))
