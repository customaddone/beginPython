# https://atcoder.jp/contests/abc146/tasks/abc146_c
a, b, x = map(int, input().split())

def solve(mid):
    ans = a * mid + b * len(str(mid))
    if ans <= x:
        return True
    else:
        return False

ok = 0
ng = 10 ** 9 + 1
# OKになるギリギリのラインを攻める
# 最後の一回でabs(ok - ng) <= 1になってもokは書き換えられない
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if solve(mid):
        ok = mid
    else:
        ng = mid
print(ok)
