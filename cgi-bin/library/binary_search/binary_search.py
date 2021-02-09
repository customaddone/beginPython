# 基本の二分探索
lista = [i for i in range(10)]

def binary_search_loop(data, target):
    imin = 0
    imax = len(data) - 1
    while imin <= imax:
        imid = imin + (imax - imin) // 2
        if target == data[imid]:
            return imid
        elif target < data[imid]:
            imax = imid - 1
        else:
            imin = imid + 1
    return False
print(binary_search_loop(lista, 4))

# 三分探索
# ARC054 ムーアの法則
def f(x):
    return x + p / pow(2, 2 * x / 3)

p = float(input())
left, right = 0, 100

while right > left + 10 ** -10:
    # mid二つ
    mid1 = (right * 2 + left) / 3
    mid2 = (right + left * 2) / 3
    if f(mid1) >= f(mid2):
        right = mid1
    else:
        left = mid2
print(f(right))

# 三分探索整数ver
num = []
for i in range(100):
    if i < 50:
        num.append(i)
    else:
        num.append(100 - i)

left, right = 0, len(num) - 1
while abs(right - left) > 3:
    mid1 = (right * 2 + left) // 3 + 1
    mid2 = (right + left * 2) // 3
    # 最小値を求める場合は矢印逆になる
    if num[mid1] <= num[mid2]:
        right = mid1
    else:
        left = mid2
print(right)
print(left)

num = [i for i in range(0, 10, 2)]
A = [2, 4, 5]
B = [2, 3]

for i in A:
    index = bisect_right(num, i)
    print(num[index - 1])

# numの中でのi未満の数字の最大値を求める
for i in A:
    index = bisect_left(num, i)
    print(num[index - 1])

# numの中でのiより大きい数字の最小値を求める
for i in B:
    index = bisect_right(num, i)
    print(num[index])

# numの中でのi以上の数字の最小値を求める
for i in B:
    index = bisect_left(num, i)
    print(num[index])
