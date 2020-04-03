# fibonacci(40)あたりから動きが怪しくなるので、メモ作っておくと便利
# 再帰は上限ある
# この方法だとfibonatti(1500)ぐらいいける
data = [0] * 100000
def fibonacci(n):
    if (n == 1) or (n == 2):
        return 1
    if data[n] != 0:
        return data[n]
    else:
        data[n] = fibonacci(n - 2) + fibonacci(n - 1)
        return data[n]

print(fibonacci(1500))
