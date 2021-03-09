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

# 天下一プログラマーコンテスト2013予選B B - 天下一後入れ先出しデータ構造

Q, L = getNM()
query = [input().split() for i in range(Q)]
s = [] # 配列の中身
l = 0 # 配列の大きさ

for q in query:
    if q[0] == "Push":
        s.append([int(q[1]), int(q[2])])
        l += int(q[1])
    if l > L:
        print("FULL")
        exit()

    elif q[0] == "Pop":
        x = int(q[1])
        l -= x
        while s: # sが空になるまで xがゼロになるとbreakで抜ける
            c, y = s[-1]
            if x >= c:
                x -= c
                s.pop() # 抜く
            else:
                s[-1][0] -= x # 引くだけで抜かない
                x = 0
                break
        if x:
            print("EMPTY")
            exit()

    elif q[0] == "Size":
        print(l)

    elif q[0] == "Top":
        if s:
            print(s[-1][1])
        else:
            print("EMPTY")
            exit()

print("SAFE")

# ヒストグラムの最大長方形

N = getN()
A = getList()

def largestRectangleArea(A):
    ans = 0
    A = [-1] + A # 最初に番兵
    A.append(-1) # 最後に番兵
    n = len(A)

    stack = [0]  # store index

    for i in range(n):
        # A[i]が一番大きくなるよう
        while A[i] < A[stack[-1]]:
            h = A[stack.pop()]
            area = h * (i - stack[-1] - 1)
            ans = max(ans, area)
        stack.append(i)
    return ans

print(largestRectangleArea(A))

# F - Many Slimes
# pop-appendleft型でソートを保てる
# 保てない場合はヒープキュー 

"""
スライムは1, 2, 4...と増える　計算量はせいぜいN**2 * 2 ** Nまでできる
簡単な場合から考える

1, 2, 3, 4
一番最初のスライムは4(一番大きいの)
3, 4 → 1, 2, 3, 4 Yesになる
もし1, 1, 3, 4でも
3, 4 → 1, 1, 3, 4 Yesになる
1, 1, 1, 4なら
1, 4 → 1, 1, 4できない

最初のスライムにはできるだけ大きい数字を産ませた方がいい
つまり一番いい状態は4, 3, 3, 3, 2, 2, 2...みたいな状態
これとSを比べて全てについて大きかったらいい？
No 5, 1, 1, 1とかの場合は5, 4, 3, 3だがYesにはならない

生産過程を木として見ると、下るにつれ数字が単調減少していく
支流を全て数え上げると判定できる？
めんどそう

最初の4, 1番目に出てきた3, 2番目に出てきた3...がゲーム終了までに何を産むか？
or ゲームのiターン目にそれぞれのスライムが何を産むか
1, 1, 1, 2, 3, 3, 3 と 4(最初)
1ターン
4は3を産む
1, 1, 1, 2, 3, 3と 3, 4
2ターン
4は3を産む
3は2を産む
1, 1, 1, 3 と2, 3, 3, 4
3ターン目　できる　
これはできそう

iターン目について手持ちのスライムがそれぞれ何を産むか(Sから何を削除するか)
はSを舐めてやる
手持ちのスライムについて、大きいものから考える　一つスケールが小さいものを選ぶ
Sは26万ぐらいあるけど、精々18周なので計算量はそんなにない
Sはpop appendleftすればソートされた順序を保てる
手持ちのスライムは無理なのでヒープキュー
"""

N = getN()
S = getList()
S.sort()

S = deque(S)
que = []
heappush(que, -S.pop())

# N回やる
for i in range(N):
    new_S = deque([])
    new_que = []
    while S and que:
        # 大きい順から取っていく
        # Sから取ったのはqueに入れる
        if S[-1] < -que[0]:
            heappush(new_que, -S.pop())
            heappush(new_que, heappop(que))
        else:
            new_S.appendleft(S.pop())
    # 整理
    while S:
        new_S.appendleft(S.pop())
    S = new_S
    que = new_que

# Sに何も残ってないと
if not S:
    print('Yes')
else:
    print('No')
