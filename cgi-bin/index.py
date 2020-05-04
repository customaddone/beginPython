# https://atcoder.jp/contests/s8pc-1/tasks/s8pc_1_e
n, q = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

mod = 10 ** 9 + 7

# 全通り使いそうなのであらかじめ列挙しとく
# べき乗にはpow便利
distance = [pow(A[i], A[i + 1], mod) for i in range(n - 1)]
# 累積和
distsum = [0]
for i in range(n - 1):
    distsum.append((distsum[i] + distance[i]) % mod)

start = 0
sum = 0
for i in C:
    walk = distsum[max(i - 1, start)] - distsum[min(i - 1, start)]
    sum += walk
    start = i - 1
# 最後帰る時
sum += distsum[max(start, 0)] - distsum[min(start, 0)]
print(sum % mod)
