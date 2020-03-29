l = int(input())
n = int(input())
x = list(map(int, input().split()))
mintime = 0
maxtime = 0
for i in range(n):
    individual = min(x[i], l - x[i])
    mintime = max(mintime, individual)
for i in range(n):
    individual = max(x[i], l - x[i])
    maxtime = max(maxtime, individual)
print(mintime)
print(maxtime)
