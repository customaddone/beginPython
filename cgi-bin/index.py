import itertools
N, K = map(int, input().split())
T = []
for i in range(N):
    t = list(map(int, input().split()))
    T.append(t)
flag = True
# 各配列のデカルト積
for ps in itertools.product(*T):
    x1 = ps[0]
    for i in range(1, N):
        x2 = ps[i]
        # 排他的論理和 x1, x2に含まれるもの - x1, x2両方に含まれるもの
        x1 = x1 ^ x2
    if x1 == 0:
        flag = False
print('Nothing' if flag else 'Found')
