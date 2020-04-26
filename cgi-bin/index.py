# https://atcoder.jp/contests/abc023/tasks/abc023_d
n = int(input())
listh = []
lists = []
for i in range(n):
    h, s = map(int, input().split())
    listh.append(h)
    lists.append(s)
left = 0
right = 10 ** 15
# 上限と下限から二分探索
# 全ての風船が時間内に到達できない線を探していく
# ある条件内に収める→二分探索が使える
for i in range(50):
    mid = (left + right) // 2
    # 時間はn分後まで
    costtime = [0] * n
    for i in range(n):
        # midに到達するまであと何分
        costtime[i] = (mid - listh[i]) / lists[i]
    # 小さい順から順に並べる
    costtime.sort()
    flag = True
    for i in range(n):
        # 1個目を割るのは0秒後
        # 2個目を割るのは1秒後
        # 3個目を割るのは2秒後...
        # 全てのcosttimeがi以内に間に合うように
        if costtime[i] - i < 0:
            flag = False
    if flag:
        right = mid
    else:
        left = mid
print(right)
