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

input = sys.stdin.readline
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
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# AGC005 C - Tree Restoring

"""
頂点数N Nは小さいが...
木です　
頂点1, 2... について最も遠い頂点がAi
距離iがいくつあるかcntする

最遠N - 1の距離が作れるのはパスグラフ
1 - 2 - 3 - 4 距離3が作れる
この時距離3は2つ、距離2は2つ
1 - 2 - 3
      - 4 の場合
距離2が3つ、距離1が1つ
まずパスグラフから考える
1 - 2 - 3 - 4 距離3が2つできる
              距離2は2つ
1 - 2 - 3 - 4
    　　　 - 5 距離3が3つできる

距離n - 1に一つ頂点をつなぐと距離nの頂点ができる
1 - 2 - 3
最初のパスグラフを作った時、max - 1, max - 2...の頂点が2個ずつできる
残った頂点を順番にパスグラフに刺していく

距離n - 1に一つ頂点をつなぐと距離nの頂点ができる
"""

N = getN()
A = getList()

distance = [0] * N
for i in range(N):
    distance[A[i]] += 1

opt = [0] * N # 現在距離iの頂点はいくつあるか
left = N # 残り頂点数
for i in range(N - 1, -1, -1):
    if distance[i] > 0:
        if distance[i] == 1: # 最遠は必ず2つ以上ある
            print('Impossible')
            exit()
        else:
            # 最初のパスグラフを引く
            for j in range(i + 1):
                left -= 1
                opt[max(i - j, j)] += 1
            break

# distance（クエリ）とopt(パスグラフ)を見比べる
for i in range(N - 1, 0, -1):
    # optは基礎的に存在する頂点
    # それを下回るようであればout
    if distance[i] < opt[i]:
        print('Impossible')
        exit()
    else:
        diff = distance[i] - opt[i]
        if diff: # 足さないといけない場合、距離がd - 1の頂点がなければいけない
            if opt[i - 1] == 0:
                print('Impossible')
                exit()
            else:
                left -= diff
                opt[i] += diff

if left == 0: # 頂点をちょうど使い切ったら
    print('Possible')
else:
    print('Impossible')

# ABC173 F - Intervals on Tree
# ある意味Unionfindか
# 新しい頂点を加えると、連結成分が1 - (既にある頂点へのエッジ)の分増える

"""
木の問題
N <= 10 ** 5
辺があると連結するので連結成分の個数が減る
L,RをnC2通り求める
bitは普通に間に合わない

やっぱり分解して考える
小さいのから
L = 1の時
R = 1 ~ N これにO(1)で答える
R = 1
1
R = 2 2は1と繋がってない
1
2 2
R = 3 3は1, 2と繋がっている
1 2 3 1

頂点1は何回数えられるか
頂点1が含まれるのは3回
頂点2が含まれるのは4回
頂点3が含まれるのは3回

木dpとか
前から順にやる？

Rで新しい数を入れると急に結合したりする
数え上げでしょう

ダブった部分を引く
全ての部分木の大きさを求めるのは無理そう
新しい要素は高々２つの要素を繋げるだけ

for i in range(N - 1):
    u, v = getNM()
    if u > v:
        u, v = v, u
    # 前に戻るエッジのみ
    dist[v - 1].append(u - 1)
for i in range(N):
    dist[i].sort()

ans = 0
for i in range(N): # L
    cnt = 0
    for j in range(i, N): # R
        # 範囲外に伸びるエッジは無視
        cnt += 1 - (len(dist[j]) - bisect_left(dist[j], i))
        ans += cnt

これはO(N ** 2)かかる
[[], [], [], [], [2], [], [1, 3, 4], [3], [0, 7], [5, 8]]
累積されていく
何もなければ1 ~ 10の累積で55のはず
しかし控除が累積して1 + 1 + 4(len([2] + len([1, 3, 4]))) + 5 + 7 + 9 = 27あるのでこれを引く
dist[4]の位置にある2はL = 1の時も引っかかる
dist[8]にある0は一回のみ引っかかって被害はN - 8 = 2

エッジが伸びることでいくら減るか
"""

N = getN()
dist = [[] for i in range(N)]
for i in range(N - 1):
    u, v = getNM()
    # 前に行くように
    if u > v:
        u, v = v, u
    dist[v - 1].append(u - 1)

ans = 0
cnt = 0
for i in range(N):
    ans += (i + 1) * (i + 2) // 2
    # distの探索
    for j in dist[i]:
        cnt += (j + 1) * (N - i)

print(ans - cnt)

# ARC028 C - 高橋王国の分割統治

"""
全方位木dpを使わない方法で
頂点iについて
iの子要素の部分木のサイズを調べる
全方位木dpの要領でやっていく
①葉から木dpしていく
②遡る
"""

N = getN()
E = [[] for i in range(N)]
for i in range(N - 1):
    p = getN()
    E[i + 1].append(p)
    E[p].append(i + 1)

# dfsする
ans = [0] * N

def dfs(u, par):
    res = 1 # 自分 + 子要素の部分木の大きさの合計
    opt_c = 0 # 子要素の部分木の大きさの最大値
    for v in E[u]:
        if v != par:
            c = dfs(v, u)
            res += c
            opt_c = max(opt_c, c)

    # 親方向の部分木の大きさはN - res
    ans[u] = max(opt_c, N - res)
    return res

dfs(0, -1)
for i in ans:
    print(i)

# ABC146 D - Coloring Edges on Tree

N = getN()

dist = [[] for i in range(N)]
edges = {}
for i in range(N - 1):
    a, b = getNM()
    dist[a - 1].append(b - 1)
    dist[b - 1].append(a - 1)
    edges[(a - 1, b - 1)] = i
    edges[(b - 1, a - 1)] = i

color = [-1] * N
color[0] = 0
ans = [0] * (N - 1)
pos = deque([0])

while pos:
    u = pos.popleft()
    j = 1
    for i in dist[u]:
        if color[i] != -1:
            continue
        if j == color[u]:
            j += 1
        color[i] = j
        ans[edges[(i, u)]] = j
        pos.append(i)
        j += 1

print(max(ans))
for i in ans:
    print(i)

# ARC108 C - Keep Graph Connected

# 一方のみ　rootを犠牲にする
# 辺にラベルがついている
# 移動先の頂点に辺の数字を書き込む

# 1の書き込み方をどうするか

N, M = getNM()
E = [[] for i in range(N)]
for i in range(M):
    u, v, c = getNM()
    E[u - 1].append([v - 1, c - 1])
    E[v - 1].append([u - 1, c - 1])

ans = [-1] * N
ans[0] = 0
q = deque([0])

while q:
    u = q.popleft()
    for v, p in E[u]:
        if ans[v] >= 0:
            continue
        # vには違う(p + 1)数字を書き込む
        if ans[u] == p:
            ans[v] = (p + 1) % N
            q.append(v)
        # vには辺の数字pを書き込む
        else:
            ans[v] = p
            q.append(v)

if -1 in ans:
    print('No')

for i in ans:
    print(i + 1)

# ABC075 C-bridge

# O(N + M)解 lowlink解
# 橋: 取り除くとグラフが連結でなくなる辺　取り除いてはいけない辺
# 後退辺: dfsする時に通らなかった辺

# 辺(u, v)について
# order[u]: uを何番目に通ったか
# low[v]: vから葉の方向に何回でも、後退辺を１回以下辿っていける点wについて、order[w]の最小値
# そもそも後退辺がない場合はlow[v] = order[v]である
# low[v] <= order[u]の場合、
# 自分より下流にある頂点が自分より上流の頂点と繋がっている = 外しても連結のままの辺
# そうではないものorder[u] < low[v]の辺(u, v)が橋

N, M = getNM()
edges = [getList() for i in range(M)]
edges = [[a - 1, b - 1] for a, b in edges]
E = [[] for i in range(N)]
for i, (a, b) in enumerate(edges):
    E[a].append([b, i])
    E[b].append([a, i])

cnt = 0
order = [-1] * N # 何番目に通ったか
e_cnt = [0] * M
# 木をdfsする
def dfs(u):
    global cnt
    # 何番目に通ったかを記録する
    order[u] = cnt
    cnt += 1
    for v, index in E[u]:
        if order[v] == -1:
            # 使った辺を記録する
            e_cnt[index] = 1
            dfs(v)

dfs(0)

low = deepcopy(order) # vからの後退辺を１回辿っていける点wについて、order[w]の最小値
for i, (a, b) in enumerate(edges):
    if e_cnt[i] == 0:
        low[a] = min(low[a], order[b])
        low[b] = min(low[b], order[a])

# lowlinkを求める
ignore = [0] * N
def lowlink(u):
    global ignore # 木ではないのでroot型ではなくignore型
    res = low[u]
    ignore[u] = 1
    for v, index in E[u]:
        if ignore[v] == 0:
            res = min(res, lowlink(v))
    low[u] = res
    return res

lowlink(0)

ans = [0] * M
for i, (a, b) in enumerate(edges):
    # 順番になるように
    if order[a] > order[b]:
        a, b = b, a
    if order[a] < low[b]:
        ans[i] += 1
print(sum(ans))
