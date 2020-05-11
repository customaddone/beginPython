N, K = map(int, input().split())
dist = [[] for i in range(N)]
A = list(map(int, input().split()))
for i in range(N):
    dist[i].append(A[i] - 1)
dp = [[0, 0] for i in range(N)]

def dfs(pos, depth):
    # 初めての訪問なら
    if dp[pos][0] == 0:
        dp[pos][0] = depth
        for i in dist[pos]:
            dfs(i, depth + 1)
    elif dp[pos][1] == 0:
        dp[pos][1] = depth
        for i in dist[pos]:
            dfs(i, depth + 1)
dfs(0, 0)
for i in range(N):
    if dp[i][0] == K or dp[i][1] == K:
        print(i + 1)
        break
    else:
        split = dp[i][1] - dp[i][0]
        if split > 0:
            if (K - dp[i][0]) % split == 0:
                print(i + 1)
                break
