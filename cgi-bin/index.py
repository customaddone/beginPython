from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import sys
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
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

from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import sys
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
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

"""
# 長さkの配列を作る
# 初項はxであり、
3 1
3 1 4
5 3 2 なら

3に +3 +1 +4 +3...していく
周期kでループする
a1 vs a2
a2 vs a3 をしていき右側の方が大きい組み合わせをカウントする
各queについてO(k)で答えればいい
あらかじめkの値を各mでmodしてもいい
3 1
3 1 4
mod 2だと
1 1 0
最初の値が1
1 + 1 = 0
0 + 1 = 1
0 + 0 = 0

nが小さければ十分いけるが ループについて考える
d > 0 かつ x + d < m ならcnt += 1
一回kを探索したらあとはループで済むようにしたい

同じ場所に同じ数で到達すればあとはループする
modがでかいんだわ
# [6, 4, 0, 4, 0, 4, 6] これの合計が次の周回でプラスされる
縦に見ていくと
[0, 4, 4, 1, 1, 5, 4] 最初の0について
この値が6 ~ 6(周期 - 1)なら数字が増えている
0 ~ 5なら増えていない
一番最初の地点になんの数字がいくつ来るか
割り切れない場合は周期はmodになる
"""

K, Q = getNM()
D = getList()
que = [getList() for i in range(Q)]
for n, x, m in que:
    d = [i % m for i in D]
    su = sum(d)
    zero = d.count(0)
    # 何回modを超えているか
    # 0の部分は控除する
    # 全体でk個(合計su)がmain回
    # そこから超えた回数(x // m)と(0の個数 * main回)を引く
    ans = 0
    main, left = divmod(n - 1, K)
    x %= m
    x += su * main
    ans += ((K - zero) * main - (x // m))
    # 残りは自分で
    x %= m
    for i in range(left):
        next = (x + d[i]) % m
        if x < next:
            ans += 1
        x = next
    print(ans)

"""
# 長さkの配列を作る
# 初項はxであり、
3 1
3 1 4
5 3 2 なら

3に +3 +1 +4 +3...していく
周期kでループする
a1 vs a2
a2 vs a3 をしていき右側の方が大きい組み合わせをカウントする
各queについてO(k)で答えればいい
あらかじめkの値を各mでmodしてもいい
3 1
3 1 4
mod 2だと
1 1 0
最初の値が1
1 + 1 = 0
0 + 1 = 1
0 + 0 = 0

nが小さければ十分いけるが ループについて考える
d > 0 かつ x + d < m ならcnt += 1
一回kを探索したらあとはループで済むようにしたい

同じ場所に同じ数で到達すればあとはループする
modがでかいんだわ
# [6, 4, 0, 4, 0, 4, 6] これの合計が次の周回でプラスされる
縦に見ていくと
[0, 4, 4, 1, 1, 5, 4] 最初の0について
この値が6 ~ 6(周期 - 1)なら数字が増えている
0 ~ 5なら増えていない
一番最初の地点になんの数字がいくつ来るか
割り切れない場合は周期はmodになる

全体から超えた回数と+0の回数を引く
"""

K, Q = getNM()
D = getList()
que = [getList() for i in range(Q)]
for n, x, m in que:
    d = [i % m for i in D]
    su = sum(d)
    zero = d.count(0)
    # 何回modを超えているか
    # 0の部分は控除する
    # 全体でk個(合計su)がmain回
    # そこから超えた回数(x // m)と(0の個数 * main回)を引く
    ans = 0
    main, left = divmod(n - 1, K)
    x %= m
    x += su * main
    ans += ((K - zero) * main - (x // m))
    # 残りは自分で
    x %= m
    for i in range(left):
        next = (x + d[i]) % m
        if x < next:
            ans += 1
        x = next
    print(ans)
