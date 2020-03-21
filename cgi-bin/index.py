# 1 pop(0)が処理される
# 2 pop(0)が処理される（一番最初から見て２つめが処理される）
# appendが処理される
n = int(input())
*a, = map(int, input().split())
for _ in range(n - 1):
    a = sorted(a)
    x = a.pop(0)
    y = a.pop(0)
    a.append((x + y)/2)
print(a[0])

# 模範解答
N=int(input())
v=sorted(map(int,input().split()))
# vの最小値
value=v[0]
for i in range(1,N):
    value=(value+v[i])/2
print(value)
