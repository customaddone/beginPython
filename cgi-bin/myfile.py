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

# 文字列操作
ABC029 C - Brute-force Attack
ABC049 C - 白昼夢

N, A, B, C = getNM()
l = getArray(N)

ans = 9999
for i in range(4 ** N):
    d = [[] for i in range(4)]
    j = i
    for k in range(N):
        d[j % 4].append(k)
        j //= 4
    mp = 0
    for j in range(3):
        if len(d[j]) == 0:
            break
        mp += abs(sum([l[k] for k in d[j]]) - A[j]) + 10 * (len(d[j]) - 1)
    else:
        ans = min(ans, mp)
print(ans)
