N = int(input())
A = list(map(int, input().split()))
alta = []
for i in range(N):
    alta.append(A[i] - (i + 1))
# 最小値を0に揃えないとバグる
plus = min(alta)
for i in range(N):
    alta[i] -= plus

def f(x):
    sum = 0
    for i in alta:
        sum += abs(x - i)
    return sum

# 極地があるので三分探索使う
left, right = 0, max(alta)
# 答えが整数になる場合このrightとleftの幅を3未満にするとバグる
while abs(right - left) > 3:
    mid1 = (right * 2 + left) // 3 + 1
    mid2 = (right + left * 2) // 3
    if f(mid1) >= f(mid2):
        # 上限を下げる（最小値をとるxはもうちょい下めの数だな）
        right = mid1
    else:
        # 下限を上げる（最小値をとるxはもうちょい上めの数だな）
        left = mid2
ans = float('inf')
for i in range(left, right + 1):
    ans = min(ans, f(i))
print(ans)
