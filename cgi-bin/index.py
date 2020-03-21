n = int(input())
*a, = map(int, input().split())
fraction = []
denominator = 1
for i in range(n):
    denominator *= a[i]
for i in range(n):
    fraction.append(denominator / a[i])
print(1/(sum(fraction)/denominator))

# 模範解答
input()
A = map(int, input().split())
print(1/sum(1/a for a in A))
