n,k=map(int, input().split())
al=[int(input()) for _ in range(n)]
INF=10**18
dp=[[INF]*(n+1) for _ in range(n)]
dp[0][0]=0
dp[0][1]=1
csum=al[0]

for i in range(1,n):
    a=al[i]
    dp[i][0]=0
    dp[i][1]=1
    for j in range(2,n+1):
        if dp[i-1][j-1]==INF:break
        need=dp[i-1][j-1]*a//csum+1
        dp[i][j]=min(dp[i-1][j],dp[i][j],dp[i-1][j-1]+need)
    csum+=a

if csum==k:
    print(1)
    exit()
# print(dp)
for i in range(n,-1,-1):
    if dp[n-1][i]<=k:
        print(i)
        break
