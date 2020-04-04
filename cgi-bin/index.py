n = int(input())
MOD = 10**4+7

# n + 1まで0
a=[0]*(max(4, n+1))
a[3]=1
# 最初にリストを作っとく
for i in range(4, n+1):
       a[i]=(a[i-1]+a[i-2]+a[i-3]) % MOD

print(a[n])
