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
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# ルートの決定方法はいじれる
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if x > y: # よりrootのインデックスが小さい方が親
            x, y = y, x
        # if self.parents[x] > self.parents[y]:
            # x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parents[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

# ARC027 B - 大事な数なのでZ回書きまLた。

"""
N桁の数字を覚えて置きたい
大文字アルファベットがそれぞれ0 ~ 9のうちのどれかの数字に対応している

Unionfindとか最大流とか
N <= 18 bit　dpまで狙える

覚えておく数字について何通り考えられるか
10 ** 18通りの数字があるがその中で？
ただし制約がある
候補を絞って全探索

アルファベットと各数字を対応させる通りは10 ** 26通り
4
1XYX
1Z48 の場合
X - Zは同じ
Y - 4は同じ
X - 8は同じ
なのでZ - 8
S1とS2に出てくる文字がどの数字と対応しているかを求めればいい

6
PRBLMB
ARC027 の時

P - A
B - C
L - 0
M - 2
B - 7
B - 7よりC - B - 7
P - AグループとRに対応する数字を求めればいい

UnionFindする
出現した文字のリスト
出現した文字が何の数字か
"""

def ord_chr(array, fanc):
    if fanc == 0:
        res = [ord(s) for s in array]
        # res = [ord(s) - ord('a') for s in array]
        return res

    if fanc == 1:
        res = [chr(i + ord('a')) for i in array]
        res = ''.join(res)
        return res

N = getN()
S1 = ord_chr(input(), 0)
S2 = ord_chr(input(), 0)

U = UnionFind(100) # 数字 + アルファベットのUnion

# まず結合
for s1, s2 in zip(S1, S2):
    if 48 <= s1 <= 57: # 数字の場合
        s1 -= 48
    else: # アルファベット
        s1 -= 65
        s1 += 10 # 数字と区別するため段差をつける
    if 48 <= s2 <= 57:
        s2 -= 48
    else:
        s2 -= 65
        s2 += 10

    U.union(s1, s2) # UnionFindは数字が小さい方がrootになるよう操作

tmp = -1 # S1の先頭の文字を記録
ans = 1
opt = set()
for i, s1 in enumerate(S1):
    if 48 <= s1 <= 57:
        s1 -= 48
    else:
        s1 -= 65
        s1 += 10

    if i == 0: # 先頭の文字について
        tmp = U.find(s1)
        # アルファベットと繋がってたら
        # 数字と結びついてたらans = 1のまま
        if tmp >= 10:
            ans = 9

    opt.add(U.find(s1))

opt.remove(tmp) # 先頭に使ったアルファベットを消す

for o in opt:
    if o >= 10: # 数字と結びついてなければ0 ~ 10を自由に選べる
        ans *= 10

print(ans)

# AtCoder Petrozavodsk Contest 001 D - Forest

"""
森です Unionfind?
森を連結にする最小コスト
制約的に最大流無理

Impossibleの条件
一つ繋ぐごとに頂点が２つ減り、森が一つ減る
森が2個以上でもう繋げなくなったらimpossible

小さい例から考える
7 5
1 2 3 4 5 6 7
3 0
4 0
1 2
1 3
5 6　の時

1 - 2 - 3 - 4 - 5
6 - 7

1と6を繋げばいい
1 - 2
3 - 4 - 5
6 - 7
の場合
motherを一つ決める(例えば1 - 2)
childは3 - 4 - 5, 6 - 7
motherの一番小さい奴とchildの一番小さい奴を消費して連結する
グループ分けする
[1, 2]
[3, 4, 5]
[6, 7] 全部ヒープキュー
小さい2つを消費(ansに加える)
併合

motherは一番でかい奴から！！！
ゆとりのある順に並べる

motherは慎重に決めないといけない
各グループの先頭列をみる
小さい順に使いたい
各グループの先頭は必ず使う
合計で2 * (g_n - 1)頂点いる
g_n - 1については各グループの先頭にしないといけない　他のは？
あとは自分以外のところから自由に　全てmotherの所有物
足すのはg_n - 1回だけでいい

groupの隣同士を併合するだけでいい
要素にグループ番号をつけて前から並べる
unionしてなかったら
motherは決めない

先頭の奴は絶対に使う
あとは小さい順から　自分以外のとこの適当なグループの先頭に繋げてやればよい

UnionFindの問題は先頭とそれ以外　という考え方をする
"""

N, M = getNM()
A = getList()
que = [getList() for i in range(M)]

# グループ分け
U = UnionFind(N)
for a, b in que:
    U.union(a, b)

group = [[] for i in range(N)]
for i in range(N):
    group[U.find(i)].append(A[i])
group = [sorted(i) for i in group if len(i) > 0]

if len(group) == 1:
    print(0)
    exit()

g_n = len(group)

ans = 0
l = []

# 先頭の絶対使う奴と二番手以降の遊撃隊に分ける
for i in range(g_n):
    ans += group[i][0]
    while len(group[i]) > 1:
        u = group[i].pop()
        l.append(u)

l.sort(reverse = True)

# 残りの頂点は小さい順
for i in range(g_n - 2):
    if l:
        u = l.pop()
        ans += u
    else:
        print('Impossible')
        exit()
print(ans)

# ABC183 F - Confluence

class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.C = [defaultdict(int) for _ in range(n)]
        self.size = [1] * n # サイズの大きさ

    def find(self,x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return

        # サイズに基づいてrootを決める
        if self.size[xRoot] < self.size[yRoot]:
            xRoot, yRoot = yRoot, xRoot

        self.parents[yRoot] = xRoot
        self.size[xRoot] += self.size[yRoot]
        self.size[yRoot] = 0

        # 小さいサイズのものを大きいサイズの方に入れる
        for k,v in self.C[yRoot].items():
            self.C[xRoot][k] += v

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

N, Q = getNM()
tree = UnionFind(N)
C = getList()

# 使いたいときは使ったらいい
for i in range(N):
    tree.C[i][C[i] - 1] += 1

for _ in range(Q):
    q, a, b = getNM()
    if q == 1:
        tree.unite(a - 1, b - 1)
    else:
        r = tree.find(a - 1)
        print(tree.C[r][b - 1])

# ABC049 D - 連結

N, K, L = getNM()
road = [getList() for i in range(K)]
line = [getList() for i in range(L)]

# 道路をやる
R = UnionFind(N)
for p, q in road:
    R.union(p - 1, q - 1)

L = UnionFind(N)
for i in range(N): # 自分がどの道路グループにいるか
    L.C[i][R.find(i)] += 1

for r, s in line:
    L.union(r - 1, s - 1)

# 自分の線路グループL.find(i)にある自分の道路グループR.find(i)の数
ans = [L.C[L.find(i)][R.find(i)] for i in range(N)]
print(*ans)

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

# ARC111 Reversible Cards
"""
N枚のカードがある
表面に見える色の種類の最大値　二分探索できない？
a, bのどちらかしか選べない　
種類の数だけでいい　貪欲？
最大数を達成する場合　どれか一枚を裏返しても他の色になるかすでに見えてる色になるか

dpも考えられる
貪欲が有力　誰が何を担当するか　レア/コモンならレアを表にすると損はない

まずaのみ表にする　ダブってるものは捨てられる
5 5 ○
5 2
5 6
1 2
9 7
2 7
4 2 ○
6 7 ○
2 2
7 8 ○
9 7
1 8
超頂点する
木になっていない集合は超頂点に繋いでまとめて１つで数える
木になっていない集合 U.size(U.root(i))(木になっていない集合の集まり + 超頂点) - 1(超頂点)
木になっている集合 U.size(U.root(i)) - 1 集合のうちどれか一つはとることができない
"""

N = getN()
ma = 10 ** 6
U = UnionFind(ma + 1)
for i in range(N):
    a, b = getNM()
    a -= 1
    b -= 1
    # aとbが同じ集合ならb = 超頂点に繋ぐ
    if U.same(a, b):
        b = ma
    U.union(a, b)

ans = 0
# 全ての色を調べる
for i in range(ma + 1):
    if i == U.find(i):
        ans += U.size(i) - 1
print(ans)
