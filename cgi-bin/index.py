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
import heapq
import math
from fractions import gcd
import random
import string
import copy
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


#############
# Main Code #
#############

# 二分探索（特定の値を求める）
lista = [i for i in range(1, 10, 2)]

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

# 2
print(binary_search_loop(lista, 5))

# 二分探索（条件を満たす値の最大値を求める）
def judge(n):
    if n < 300:
        return True
    else:
        return False

ok = -1
ng = 10 ** 9 + 1
# OKになるギリギリのラインを攻める
# 最後の一回でabs(ok - ng) <= 1になってもokは書き換えられない
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if judge(mid):
        ok = mid
    else:
        ng = mid

# 299 NGは300
print(ok)

# 二分探索（条件を満たす値の最大値を求める）
# 複雑なパターン
N = 5
A = [2, 4, 6, 19, 17]

ng = -1
ok = 10 ** 12 + 1

# 超えてはいけないラインを設定
def judge(limit):
    flag = True
    for i in range(N):
        if A[i] > limit:
            flag = False
            break

    return flag

while ok - ng > 1:
    mid = (ok + ng) // 2
    # 差がK以下であれば修正可能
    # もうちょい下のmidも試してみる
    if judge(mid):
        ok = mid
    else:
        ng = mid
# 19
print(ok)

# 三分探索整数ver
num = []
for i in range(100):
    if i < 50:
        num.append(i)
    else:
        num.append(100 - i)

left, right = 0, len(num) - 1
while abs(right - left) > 3:
    mid1 = (right * 2 + left) // 3 + 1
    mid2 = (right + left * 2) // 3
    # 最小値を求める場合は矢印逆になる
    if num[mid1] <= num[mid2]:
        right = mid1
    else:
        left = mid2

# どうしても間は３つ空く
# 51
print(right)
# 48
print(left)

# 三分探索小数点以下ver
def f(x):
    # これの最小値を求める
    return x + p / pow(2, 2 * x / 3)

p = 50
left, right = 0, 100

while right > left + 10 ** -10:
    mid1 = (right * 2 + left) / 3
    mid2 = (right + left * 2) / 3
    if f(mid1) >= f(mid2):
        # 上限を下げる（最小値をとるxはもうちょい下めの数だな）
        right = mid1
    else:
        # 下限を上げる（最小値をとるxはもうちょい上めの数だな）
        left = mid2

# 8.959233535496452
print(f(right))
