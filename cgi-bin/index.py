# N <= 8 O(2^N * N!)解法　前から全部足して条件を満たすか
# N <= 20 O(2^N)解法　締め切りの近い順にソートして全部足して条件を満たすか
# N <= 5000 任意のiについて Di = 5000 O(NmaxD)解法　ナップサックする　ソートしなくていい
# N <= 5000 O(NmaxD)解法　O(NmaxD)解法　
# dp[i][j]: i日目までに締め切りを迎える仕事のみでナップサック ソートをする

N = int(input())
I = [list(map(int, input().split())) for i in range(N)]
I.sort()

prev = defaultdict(int)
prev[0] = 0

for d, c, s in I:
    next = deepcopy(prev)
    for w, v in prev.items():
        if w + c <= d:
            next[w + c] = max(next[w + c], s + v)
    prev = next

ans = 0
for v in prev.values():
    ans = max(ans, v)

print(ans)
