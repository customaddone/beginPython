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

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############


logk = Q.bit_length() - 1
doubling = [[-1] * N for _ in range(logk)]

# doubling[0][i]: 回数、場所
for i in range(N): # 1回目の移動
    if S[i] == P[0]:
        if D[0] == 'L':
            doubling[0][i] = i - 1
        else:
            doubling[0][i] = i + 1
    else:
        doubling[0][i] = i

for i in range(1, logk): # 2回目以降
    for j in range(N):
        if 0 <= doubling[i - 1][j] < N: # 範囲内にある場合
            if S[1 << i] == P[1 << i]: # 一致
                if D[1 << i] == 'L':
                    doubling[i][j] = doubling[i - 1][doubling[i - 1][j]] - 1
                else:
                    doubling[i][j] = doubling[i - 1][doubling[i - 1][j]] + 1
            else: # 一致しない
                doubling[i][j] = doubling[i - 1][doubling[i - 1][j]]
        else: # 範囲内にない場合は欄外
            doubling[i][j] = doubling[i - 1][j]
