
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

# list
str = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
rev = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
# 文字列を整数に変換
# 26進数

N = 26

def num2alpha(num):
    if num <= 26:
        return chr(96 + num)
    elif num % 26 == 0:
        return num2alpha(num // 26 - 1) + chr(122)
    else:
        return num2alpha(num // 26) + chr(96 + num % 26)

# z
print(num2alpha(N))

n = N
lista = []
digit = 26
i = 0

while n != 0:
    opt = n % digit
    lista.insert(0, opt)
    if n % digit == 0:
        n = n // digit - 1
    else:
        n = n // digit
    i += 1

str_list = 'abcdefghijklmnopqrstuvwxyz'
ans = ''
for i in range(len(lista)):
    ans += str_list[lista[i] - 1]

# z
print(ans)

# 文字配列を数字配列に
# pypyだといる

def ord_chr(array, fanc):
    if fanc == 0:
        res = [ord(s) - ord('a') for s in array]
        return res

    if fanc == 1:
        res = [chr(i + ord('a')) for i in array]
        res = ''.join(res)
        return res
