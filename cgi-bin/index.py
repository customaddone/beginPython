import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

## square869120Contest #1 G

N, M = mi()
if N==1:
    print(0, 1)
    exit()
rel = [[] for _ in range(N)]

for i in range(M):
    s, t, c, lim = mi()
    s, t = s-1, t-1
    rel[s].append((t, c, lim))
    rel[t].append((s, c, lim))
B = 2**N

dp = dp2(float('inf'), N, B)
dp[0][0] = 0
cnt = dp2(0, N, B)
cnt[0][0] = 1
for state in range(B-1):
    for now in range(N):
        for t, c, lim in rel[now]:
            if dp[state][now] != float('inf'):
                if not state & 1<<t and dp[state][now]+c <= lim:
                    if t == 0 and state+1 < B-1:
                        continue
                    if dp[state|1<<t][t] == dp[state][now]+c:
                        #print(state, now)
                        cnt[state|1<<t][t] += cnt[state][now]
                    if dp[state|1<<t][t] > dp[state][now]+c:
                        dp[state|1<<t][t] = dp[state][now] + c
                        cnt[state|1<<t][t] = cnt[state][now]
#print(cnt)
#print(dp)
if dp[B-1][0] == float('inf'):
    print('IMPOSSIBLE')
    exit()
print(dp[B-1][0], cnt[B-1][0])
