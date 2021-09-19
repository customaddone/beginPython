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
sys.setrecursionlimit(1000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# https://qiita.com/Morifolium/items/6c8f0a188af2f9620db2
N = 8

ab = [
[1, 6],
[2, 5],
[3, 1],
[3, 2],
[4, 1],
[4, 6],
[5, 1],
[6, 7],
[7, 8]
]
"""
for _ in range(N + M - 1):
    ab.append(tuple(map(int, input().split())))
"""

def topological(n, dist):
    in_cnt = defaultdict(int)
    outs = defaultdict(list)

    for a, b in ab:
        in_cnt[b - 1] += 1
        outs[a - 1].append(b - 1)

    res = []
    queue = deque([i for i in range(n) if in_cnt[i] == 0])

    while len(queue) != 0:
        v = queue.popleft()
        res.append(v)
        for v2 in outs[v]:
            in_cnt[v2] -= 1
            if in_cnt[v2] == 0:
                queue.append(v2)

    return res

# [2, 3, 1, 4, 0, 5, 6, 7]
# queryに閉路ができる道を追加するとバグってlen = 8未満の配列を返す
print(topological(N, ab))

# ABC041 D - 徒競走
# トポロジカルソートの種類の数
N, M = 3, 2
query = [
[2, 1],
[2, 3]
]

X = [0] * N
for i in range(M):
    x, y = query[i]
    # xにある矢印を集計
    X[x - 1] |= 1 << (y - 1)

DP = [0] * (1 << N)
DP[0] = 1

# jの左に置くものとしてどのような組み合わせがあるか
for bit in range(1, 1 << N):
    for j in range(N):
        # j番目が含まれる場合において
        if bit & (1 << j):
            if not (X[j] & (bit ^ (1 << j))):
                # 上のbitまで運送してってdp[-1]で集計
                DP[bit] += DP[bit ^ (1 << j)]
print(DP)

# 全国統一プログラミング王決定戦予選 D - Restore the Tree

"""
元のN頂点N - 1辺の根付き有向辺グラフ + 新たにM本の有向辺
元の木は一意に定まることが示せる。

邪魔なM本を消せ
木にするためには
ループを消す
B側に根以外の各頂点がN - 1個あるようにすればいい
他には？
適当に辺を選んでいくが、最終的に連結である必要がある

6 3
2 1
2 3
4 1
4 2
6 1
2 6
4 6
6 5の場合

1: [2, 1], [4, 1], [6, 1]
2: [4, 2]
3: [6, 3]
4: [] 親になるものがすぐわかることもある
5: [6, 5]
6: [2, 6], [4, 6]

切り離しても連結のママのものは？
MのA,Bについて、Bは元の根付き木に置けるAの子孫である
親方向へは伸びない
なのでトポソする
"""

N, M = getNM()
dist = [getList() for i in range(N + M - 1)]
edges = [[] for i in range(N)] # 親要素の候補
for a, b in dist:
    edges[b - 1].append(a - 1)

# トポソする
# 順番が求まる
res = topological(N, dist)

ans = [-1] * N
ans[res[0]] = 0
depth = [-1] * N
depth[res[0]] = 0

# 追加のM辺はショートカットになるので
# 元の根付き木は辺のうち深さが最も深くなるもの

for i in res[1:]: # 二番手以降について調べる
    parent = 0
    dep_opt = 0
    for j in edges[i]: # iの各親について深さを調べる
        if depth[j] + 1 > dep_opt: # 更新できるなら
            parent = j
            dep_opt = depth[j] + 1
    ans[i] = parent + 1
    depth[i] = dep_opt

for i in ans:
    print(i)

# 0-index
def topological(n, dist):
    in_cnt = defaultdict(int)
    outs = defaultdict(list)

    for a, b in dist:
        in_cnt[b] += 1
        outs[a].append(b)

    res = []
    queue = deque([i for i in range(n) if in_cnt[i] == 0])

    while len(queue) != 0:
        v = queue.popleft()
        res.append(v)
        for v2 in outs[v]:
            in_cnt[v2] -= 1
            if in_cnt[v2] == 0:
                queue.append(v2)

    return res

# codeforces # 656
# E-Directing Edges

# 連結かどうかはわからない
# 無効辺については全て方向を決める
# ループがないようにしたい
# 有効辺については確定している　
# DAGになるということ
# 最善のやり方がある　それでもできなければNO
# トポロジカルになっているということ　これより後の頂点の方向に結ぶ
# まとめてやる　入次数が0のものから
# 無効辺は有効辺 * 2にする？

# トポソする　無効辺はどうする
# トポソ頂点→トポソ頂点、トポソ頂点→無頂点、無頂点→無頂点
# トポソして方向決めてもう一回トポソする

T = getN()
for _ in range(T):
    N, M = getNM()

    und = [[] for i in range(N)]
    dir = []
    in_cnt = defaultdict(int)
    outs = defaultdict(list)
    ans = {}

    # divide undirected and directed path
    for i in range(M):
        t, a, b = getNM()
        # undirected
        if t == 0:
            und[a - 1].append([i, b - 1])
            und[b - 1].append([i, a - 1])
        # directed
        else:
            ans[i] = (a, b)
            dir.append([a - 1, b - 1])

    # if directed-only graph is acyclic, can see all vertices
    order = topological(N, dir)
    # determine the directions of undirected edges
    for u in order:
        for ind, v in und[u]:
            # used or not?
            if not ind in ans:
                dir.append([u, v])
                ans[ind] = (u + 1, v + 1)

    # whether if the resulting graph is directed and acyclic
    if len(topological(N, dir)) < N:
        print('NO')
    else:
        print('YES')
        for k, v in sorted(ans.items()):
            print(*v)

# codeforces #743 C. Book
# 前から読み続けた場合
# 入次数管理とheapqueを使ってトポソする
# 現在探索しているのより前にある頂点はnextに、後にあるのはprevにappend

"""
この章を理解するためには他の章を理解しないといけない　トポロジカル？
前から何回も読む　何回で全て理解できるか
ループがあれば永遠に理解できない

トポソして前からdp
まず入次数0のものを全て取り除く
そして入次数を引く
また0になったものを取り除く...
引いて0になったものを押さえておく
最初読めなくてもループの途中でも読めるようになる
順番は守ろう
"""

T = getN()
for _ in range(T):
    N = getN()
    E = [[] for i in range(N)]
    cnt = [0] * N

    for v in range(N):
        k = getList()
        cnt[v] = k[0]
        for u in k[1:]:
            E[u - 1].append(v)

    prev = [i for i in range(N) if cnt[i] == 0]
    heapify(prev)

    ans, ignore = 0, 0
    while prev:
        next = []
        ans += 1
        while prev:
            u = heappop(prev)
            ignore += 1
            for v in E[u]:
                cnt[v] -= 1
                if cnt[v] == 0:
                    # 探索したのより前にあれば次回
                    if v < u:
                        heappush(next, v)
                    else:
                        heappush(prev, v)

        prev = next

    if ignore == N:
        print(ans)
    else:
        print(-1)
