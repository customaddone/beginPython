n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
lat = 0
abstem = 1000
for i in range(n):
    avetem = t - h[i] * 0.006
    if abs(avetem - a) <= abstem:
        abstem = abs(a - avetem)
        lat = h[i]
print(h.index(lat) + 1)

# 模範解答
n=int(input())
t,a=map(int,input().split())
h=list(map(int,input().split()))
z = [abs(t - i * 0.006 - a) for i in h]
print(z.index(min(z)) + 1)
