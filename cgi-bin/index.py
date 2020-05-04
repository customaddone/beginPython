# https://atcoder.jp/contests/nikkei2019-final/tasks/nikkei2019_final_a
n = int(input())
A = list(map(int, input().split()))
# 累積和
listsum = [0]
for i in range(n):
    listsum.append(listsum[i] + A[i])
ans = []
for i in range(n):
    res = 0
    # 範囲はlistsum(n + 1) - 幅の大きさ(i + 1)
    for j in range(n - i):
        # listsum[j + 幅] - listsum[i]
        opt = listsum[j + i + 1] - listsum[j]
        res = max(res, opt)
    ans.append(res)
for i in ans:
    print(i)
