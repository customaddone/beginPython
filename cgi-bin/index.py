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

from collections import defaultdict, deque, Counter
from sys import exit
import heapq
import math
import fractions
import copy
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

S = input()
N = len(S)
modlist = [0] * 13
splitmod = []

if S[0] == "?":
    for i in range(10):
        modlist[i % 13] += 1
else:
    modlist[int(S[0])] += 1
S = S[1:]

# 前から処理していく
# 10と13は互いに素なので
# a == b (mod z)なら
# 10a == 10b (mod z)
# 例
# 18 == 5 (mod 13)
# 180 == 50 (mod 13)
# 13 * 13 + 11 == 13 * 3 + 11 (mod 13)
for st in S:
    modalta = [0] * 13
    if st == "?":
        # 例えば 7?4の時
        # 7 * 10 + 1, 2, 3...
        for i in range(10):
            # modlist
            for j in range(13):
                opt = (j * 10 + i) % 13
                modalta[opt] += modlist[j]
    else:
        for j in range(13):
            opt = (j * 10 + int(st)) % 13
            modalta[opt] += modlist[j]
    # mod調整
    for i in range(13):
        modalta[i] %= mod
    modlist = copy.deepcopy(modalta)

print(modlist[5] % mod)
