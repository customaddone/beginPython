# https://atcoder.jp/contests/abc002/tasks/abc002_3
xa, ya, xb, yb, xc, yc = map(int, input().split())
x1, y1 = (xb - xa), (yb - ya)
x2, y2 = (xc - xa), (yc - ya)
# 3点(0, 0),(a, b),(c, d)で構成される三角形の面積は|ad - bc|/2
ans = abs(x1 * y2 - y1 * x2) / 2
print(ans)
