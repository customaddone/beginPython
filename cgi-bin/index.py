import collections

N = int(input())
A = list(map(int, input().split()))
# collections.Counter(A)で速くなる！！
cnt = collections.Counter(A)
for i in range(1, N+1):
    print(cnt[i])
