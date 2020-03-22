# 全員をスタート地点から都市１に移動させるのにn // time[0] + 1分かかる
# 全員をスタート地点から都市２に移動させるのに上記 + (n % time[i]) // time[1]分かかる
# ...
n = int(input())
time = [int(input()) for _ in range(5)]
result = 0
for i in range(5):
    result += (n // time[i])
    result += 1
    n = n % time[i]
print(result)

# 模範解答 最初っからminで
import math
n=int(input())
l=[int(input()) for i in range(5)]
print(math.ceil(n/min(l))+4)
