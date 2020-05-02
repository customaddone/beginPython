n, m, q = map(int, input().split())
point = []
for i in range(q):
    a, b, c, d = map(int, input().split())
    point.append([a - 1, b - 1, c, d])

def dfs(pos, a, m, point):
    # posがaの配列の長さと同じになったら
    if pos == len(a):
        sc = 0
        for co in point:
            # 得点計算
            if a[co[1]] - a[co[0]] == co[2]:
                sc += co[3]
        return sc
    ans = 0
    if pos == 0:
        low = 0
    else:
        low =  a[pos - 1]
    # mはaの各要素の上限
    for i in range(low, m + 1):
        print([pos, i])
        a[pos] = i
        ans = max(ans, dfs(pos+1, a, m, point))
    return ans
# posは最初0, aも[0] * n
print(dfs(0, [0] * n, m, point))
