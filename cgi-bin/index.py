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

N = getN()
S1 = input()
S2 = input()
str_c = [0] * 26 # 文字が出現したか
number = [-1] * 26 # どの文字が割り当てられているか
ascii_uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

U = UnionFind(26)
# 通りが0の場合もあるが
for i in range(N):
    # 両方文字ならグループ化
    if (S1[i] in ascii_uppercase) and (S2[i] in ascii_uppercase):
        str_c[ord(S1[i]) - ord('A')] = 1
        str_c[ord(S2[i]) - ord('A')] = 1
        U.union(ord(S1[i]) - ord('A'), ord(S2[i]) - ord('A'))
    if not (S1[i] in ascii_uppercase) and not (S2[i] in ascii_uppercase):
        if int(S1[i]) != int(S2[i]): # そもそも数字同士が違う
            print(0)
            exit()

# グループ化し終わったら数字を対応させる
# あるグループにアクセスするときはU.find(i)でアクセスする
# するとグループの代表者が出てきてくれる
# そのグループの代表者にどの文字と対応しているか、先頭の文字かを尋ねる
for i in range(N):
    if (S1[i] in ascii_uppercase) and not (S2[i] in ascii_uppercase): # S1が文字
        str_c[ord(S1[i]) - ord('A')] = 1
        if number[U.find(ord(S1[i]) - ord('A'))] == -1: # 未登録
            number[U.find(ord(S1[i]) - ord('A'))] = int(S2[i])
        else:
            if number[U.find(ord(S1[i]) - ord('A'))] != int(S2[i]): # 矛盾する
                print(0)
                exit()

    if not (S1[i] in ascii_uppercase) and (S2[i] in ascii_uppercase): # S2が文字
        str_c[ord(S2[i]) - ord('A')] = 1
        if number[U.find(ord(S2[i]) - ord('A'))] == -1:
            number[U.find(ord(S2[i]) - ord('A'))] = int(S1[i])
        else:
            if number[U.find(ord(S2[i]) - ord('A'))] != int(S1[i]):
                print(0)
                exit()

first = [0] * 26 # 一番前の数字か
if (S1[0] in ascii_uppercase):
    first[U.find(ord(S1[0]) - ord('A'))] = 1
    if number[U.find(ord(S1[0]) - ord('A'))] == 0: # 一番最初の文字に0が登録されていたら
        print(0)
        exit()

if (S2[0] in ascii_uppercase):
    first[U.find(ord(S2[0]) - ord('A'))] = 1
    if number[U.find(ord(S2[0]) - ord('A'))] == 0:
        print(0)
        exit()

ans = 1
# 未登録の数字については0 ~ 9または1 ~ 9になる可能性がある
for i in range(26):
    if str_c[i] and number[U.find(i)] == -1: # 未登録なら
        if first[U.find(i)]:
            ans *= 9 # 1 ~ 9
            number[U.find(i)] = 10
        else:
            ans *= 10
            number[U.find(i)] = 11

print(ans)
