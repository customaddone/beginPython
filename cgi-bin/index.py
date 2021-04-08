N = int(input())
P = [list(map(int, input().split())) for i in range(N)]
eps = 10 ** (-10)
import math

def euc(p1, p2): # 二点のユークリッド距離を求める
    px1, py1 = p1
    px2, py2 = p2
    return math.sqrt((px2 - px1) ** 2 + (py2 - py1) ** 2)

def angle(c, p): # 線分cpとcからx軸の正の部分と平行に伸びる半直線とのなす角の大きさ
    d = euc(c, p)
    x = (p[0] - c[0]) / d
    y = (p[1] - c[1]) / d
    if y >= 0:
        return math.degrees(math.acos(x))
    else:
        return 360 - math.degrees(math.acos(x))

ans = float('inf') # 180度との差　これを最小に
for i in range(N): # 点P[i]を中心に各線分について
    l = []
    for j in range(N):
        if i == j:
            continue
        opt = angle(P[i], P[j])
        l.append(opt)
        l.append(opt + 360) #　一周後の
    l.sort()

    now = 0
    for j in range(N - 1): # 尺取り法 線分はN - 1本できるのでそれぞれについて
        while l[now] < l[j] + 180 + eps:
            now += 1
        ans = min(ans, abs(180 - (l[now] - l[j])), abs(180 - (l[now - 1] - l[j])))

print(180 - ans)
