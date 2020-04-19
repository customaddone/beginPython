t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

for bi in b:
    sellable = False
    # jはajのインデックス
    for j, aj in enumerate(a):
        if t >= bi - aj >= 0:
            # a[j]の値を100000にして使えないようにする
            a[j] = 100000
            sellable = True
            break
    if not sellable:
        print('no')
        break
else:
    print('yes')
