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

par = [-1] * N
depth = [-1] * N
depth[0] = 0
pos = deque([0])
while pos:
    u = pos.popleft()
    for i in E[u]:
        if depth[i] == -1:
            depth[i] = depth[u] + 1
            par[i] = u
            pos.append(i)

logk = max(depth).bit_length()

doubling = [[-1] * N for _ in range(logk)]
for i in range(N):
    doubling[0][i] = par[i]

for i in range(1, logk):
    for j in range(N):
        if doubling[i - 1][j] == -2:
            doubling[i][j] = -2
        else:
            doubling[i][j] = doubling[i - 1][doubling[i - 1][j]]

Q = getN()
for i in range(Q):
    t, e, x = getNM()
    if t == 1:
        a, b = edges[e - 1]
    else:
        b, a = edges[e - 1]

    dep_diff = depth[a] - depth[b]

    # aがbの親か
    if dep_diff > 0:
        now = a
        for i in range(logk):
            if dep_diff & (1 << i):
                now = doubling[i][now]
        if now == b:
            print('Yes')
        else:
            print('No')
    # bがaの親か
    else:
        dep_diff *= -1
        now = b
        for i in range(logk):
            if dep_diff & (1 << i):
                now = doubling[i][now]
        if now == a:
            print(a, b, 'Yes')
        else:
            print('No')
