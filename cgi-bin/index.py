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
from itertools import combinations, permutations, product
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


#############
# Main Code #
#############

def rand_letter(size):
    ascii_original='ox'
    digits_original='01'

    digits='0123456789'
    ascii_lowercase='abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # 好きなものを使ってね
    psuedo = ascii_original

    return ''.join([random.choice(psuedo) for i in range(size)])

N = getN()
S = input()
lista = ['SS', 'SW', 'WS', 'WW']

def judge(string):
    alta = copy.deepcopy(string)
    for i in range(1, N - 1):
        if alta[-1] == "S" and alta[-2] == "S":
            if S[i] == "o":
                alta.append('S')
            else:
                alta.append("W")
        elif alta[-1] == "S" and alta[-2] == "W":
            if S[i] == "o":
                alta.append('W')
            else:
                alta.append("S")
        elif alta[-1] == "W" and alta[-2] == "S":
            if S[i] == "o":
                alta.append('W')
            else:
                alta.append("S")
        else:
            if S[i] == "o":
                alta.append('S')
            else:
                alta.append("W")

    return alta

def judge_2(before, now, after, j):
    if now == "S":
        if j == "o":
            if before == after:
                return True

        else:
            if before != after:
                return True

    else:
        if j == "o":
            if before != after:
                return True

        else:
            if before == after:
                return True
    return False

for i in lista:
    opt = judge(list(i))
    if judge_2(opt[-2], opt[-1], opt[0], S[-1]) and judge_2(opt[-1], opt[0], opt[1], S[0]):
        print(''.join(opt))
        exit()
print(-1)
