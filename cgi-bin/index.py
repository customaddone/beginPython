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

# p135 subsequence
N = 10
S = 15
A = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
right = 0
total = 0
ans = float('inf')

for left in range(N):
    while right < N and total < S:
        total += A[right]
        right += 1

    if total < S:
        continue

    ans = min(ans, right - left)

    if left == right:
        right += 1
    total -= A[left]

print(ans)

# p137 Jessica's Reading Problem
P = 5
A = [1, 8, 8, 8, 1]
dict = {}
for i in A:
    dict[i] = 0

l = 0
cnt = 0
ans = float('inf')
# 右を一つ進めて左をできる限り進める
for r in range(P):
    # 新しく一つ加える
    if dict[A[r]] == 0: # 新しい要素が来たなら
        cnt += 1
    dict[A[r]] += 1

    # 全ての要素を含む条件で左を削っていく
    while True:
        # もし要素が１つしか無かったら削れない
        if dict[A[l]] == 1:
            break
        # 要素が２つ以上あれば削る
        dict[A[l]] -= 1
        l += 1

    if cnt < len(dict.items()):
        continue

    ans = min(ans, r - l + 1)
print(ans)

# p138 Face The Right Way
N = 7
S = 'BBFBFBB'

def judge(k):
    imos = [0] * N
    if S[0] == 'B':
        imos[0] = 1
    # ひっくり返していく
    for i in range(1, N - k + 1):
        if i < k:
            rev = imos[i - 1]
        else:
            rev = imos[i - 1] - imos[i - k]
        if (S[i] == 'B') ^ (rev % 2):
            imos[i] += 1
        imos[i] += imos[i - 1]

    # 残りのものが合っているか調べる
    for i in range(N - k + 1, N):
        if i < k:
            rev = imos[N - k]
        else:
            rev = imos[N - k] - imos[i - k]
        if (S[i] == 'B') ^ (rev % 2):
            return float('inf')

    return imos[N - k]

K = 0
M = float('inf')
for i in range(1, N + 1):
    opt = judge(i)
    if opt < M:
        M = opt
        K = i
print(K, M)

# p141 Fliptile
M = 4
N = 4
maze = [
[1, 0, 0, 1],
[0, 1, 1, 0],
[0, 1, 1, 0],
[1, 0, 0, 1]
]

def changer(o, f):
    for i in range(1, M):
        for j in range(N):
            # 一つ上のmazeとflipを調べる
            # mazeが黒 and flipが偶数回ひっくりかえる or mazeが白 and flipが奇数回ひっくりかえるなら
            if (maze[i - 1][j] == 1) ^ (f[i - 1][j] % 2):
                o[i][j] += 1
                f[i][j] += 1
                f[i - 1][j] += 1
                if j >= 1:
                    f[i][j - 1] += 1
                if j < N - 1:
                    f[i][j + 1] += 1
                if i < M - 1:
                    f[i + 1][j] += 1

    return o, f

# １行目について全探索
# O(MN(2 ** N))になる
for bit in range(1 << N):
    opt = [[0] * N for i in range(M)]
    flip = [[0] * N for i in range(M)]
    for i in range(N):
        if bit & (1 << i):
            opt[0][i] += 1
            flip[0][i] += 1
            if i >= 1:
                flip[0][i - 1] += 1
            if i < N - 1:
                flip[0][i + 1] += 1

    opt, flip = changer(opt, flip)

    # 最後の列について判定
    for j in range(N):
        # 違うなら
        if (maze[M - 1][j] == 1) ^ (flip[M - 1][j] % 2):
            break
    else:
        print(opt)

# p145 physics experiment
# antsと同じく玉同士はすり抜けるものとして考える
N, H, R, T = 2, 10, 10, 100
g = 10

def judge(time):
    if time < 0:
        return H
    t = math.sqrt(2 * H / 10)
    k = int(time / t)
    if k % 2 == 0:
        d = time - k * t
        return H - g * d * d / 2
    else:
        d = k * t + t - time
        return H - g * d * d / 2

ans = []
for i in range(N):
    # 一秒ごとにボールを落下させる
    ans.append(judge(T - i))
# ボールは互いにすり抜けるものと考えて良い
ans.sort()
for i in range(N):
    # RはセンチメートルだがHはメートル
    print(ans[i] + (2 * R * i / 100))

# p147 4 values whose sum is 0
def binary_search_loop(data, target):
    imin = 0
    imax = len(data) - 1
    while imin <= imax:
        imid = imin + (imax - imin) // 2
        if target == data[imid]:
            return imid
        elif target < data[imid]:
            imax = imid - 1
        else:
            imin = imid + 1
    return False

N = 6
A = [-45, -41, -36, -36, 26, -32]
B = [22, -27, 53, 30, -38, -54]
C = [42, 56, -37, 75, -10, -6]
D = [-16, 30, 77, -46, 62, 45]

re_A = []
re_C = []
for i in range(N):
    for j in range(N):
        re_A.append(A[i] + B[j])
re_A.sort()

for i in range(N):
    for j in range(N):
        re_C.append(C[i] + D[j])
re_C.sort()

ans = 0
for i in re_A:
    # 該当する数字があった場合の左端
    ind1 = bisect_left(re_C, 0 - i)
    # 右端
    ind2 = bisect_left(re_C, 0 - i + 1)
    ans += ind2 - ind1
print(ans)

# p148 巨大ナップサック
N = 4
w = [2, 1, 3, 2]
v = [3, 2, 4, 2]
W = 5

# 半分全列挙 + 二分探索
def re_list(weight, value):
    fore_list = []
    # まず全通り組み合わせる
    for bit in range(1 << len(weight)):
        wei = 0
        val = 0
        for i in range(len(weight)):
            if bit & (1 << i):
                wei += weight[i]
                val += value[i]
        fore_list.append([wei, val])
    fore_list.sort()

    # リスト再作成
    # 明らかにいらないものは消している
    alta_w = []
    alta_v = []
    now = -1
    for i in fore_list:
        if now < i[1]:
            now = i[1]
            alta_w.append(i[0])
            alta_v.append(i[1])
    return alta_w, alta_v

def half_knapsack(N, limit, weight, value):
    # 半分全列挙
    fore_w, fore_v = re_list(weight[:N // 2], value[:N // 2])
    back_w, back_v = re_list(weight[N // 2:], value[N // 2:])

    ans = 0
    for b_w, b_v in zip(back_w, back_v):
        if b_w > limit:
            continue

        opt = b_v
        index = bisect_right(fore_w, limit - b_w)
        if index > 0:
            opt += fore_v[index - 1]
        ans = max(ans, opt)

    return ans
print(half_knapsack(N, W, w, v))

# 実は今回の問題では全く圧縮されないんです
W, H, N = 10, 10, 5
# (x1, y1)から(x2, y2)まで線を引く
X1 = [i - 1 for i in [1, 1, 4, 9, 10]]
X2 = [i - 1 for i in [6, 10, 4, 9, 10]]
Y1 = [i - 1 for i in [4, 8, 1, 1, 6]]
Y2 = [i - 1 for i in [4, 8, 10, 5, 10]]

# 縦
row = set()
r_index = {}
# 横
col = set()
c_index = {}
# 変換
for x, y in zip(X1 + X2, Y1 + Y2):
    # どの横列が必要か
    row.add(y)
    if y > 0:
        row.add(y - 1)
    if y < H:
        row.add(y + 1)

    # どの縦列が必要か
    col.add(x)
    if x > 0:
        col.add(x - 1)
    if x < W:
        col.add(x + 1)

# 圧縮後のどの座標になるか
row = sorted(list(row))
for i in range(len(row)):
    r_index[row[i]] = i

col = sorted(list(col))
for i in range(len(col)):
    c_index[col[i]] = i

X1 = [c_index[i] for i in X1]
X2 = [c_index[i] for i in X2]
Y1 = [r_index[i] for i in Y1]
Y2 = [r_index[i] for i in Y2]

print(X1, X2, Y1, Y2)

#  以下省略
dp = [[0] * len(col) for i in range(len(row))]
