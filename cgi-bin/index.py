def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


#############
# Main Code #
#############

# y = line[0]x + line[1]
# 傾きmaxならx = line[3]
def line(Ax, Ay, Bx, By):
    if Ay == By:
        return 0, Ay, None
    if Ax == Bx:
        return float("inf"), 0, Ax
    a = (Ay - By) / (Ax - Bx)
    b = Ay - a * Ax
    return a, b, None

# print(line(0, 2, 1, 3))
# 二つの線がクロスするx,y座標を出す
def cross(l1, l2):
    a1, b1, xx1 = min(l1, l2)
    a2, b2, xx2 = max(l1, l2)
    if a1 == a2:
        return None
    if a2 == float("inf"):
        x = xx2
    else:
        x = (b1 - b2) / (a2 - a1)
    y = a1 * x + b1
    return x, y

Ax, Ay, Bx, By = getNM()
N = getN()
P = [tuple(getNM()) for _ in range(N)]
P += [P[0]]
chop = line(Ax, Ay, Bx, By)
ans = 0
for i in range(N):
    p1 = P[i]
    p2 = P[i + 1]
    side = line(p1[0], p1[1], p2[0], p2[1])
    c = cross(chop, side)
    if not c:
        continue
    x, y = c
    if min(p1[0], p2[0]) <= x <= max(p1[0], p2[0]) and min(Ax, Bx) <= x <= max(Ax, Bx):
        ans += 1
print(ans // 2 + 1)
