# https://atcoder.jp/contests/arc054/tasks/arc054_b
# 三分探索
# 二分探索は零点を求めるのに使われるのに対し、三分探索は極値を求めるのに使われる．
# 極限が１つ以下の関数のとき使ってね
def f(x):
    # これの最小値を求める
    return x + p / pow(2, 2 * x / 3)

p = float(input())
left, right = 0, 100
while right > left + 10 ** -10:
    mid1 = (right * 2 + left) / 3
    mid2 = (right + left * 2) / 3
    if f(mid1) >= f(mid2):
        # 上限を下げる（最小値をとるxはもうちょい下めの数だな）
        right = mid1
    else:
        # 下限を上げる（最小値をとるxはもうちょい上めの数だな）
        left = mid2
print(f(right))
