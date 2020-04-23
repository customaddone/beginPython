# https://atcoder.jp/contests/abc152/tasks/abc152_d
n = int(input())
cnt = 0
# うまく個性を捨てよう
memo = [[0] * 10 for i in range(10)]
for i in range(1, n + 1):
    memo[int(str(i)[0])][int(str(i)[-1])] += 1
for i in range(10):
    for j in range(10):
        cnt += memo[i][j] * memo[j][i]
print(cnt)
