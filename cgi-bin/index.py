import math
n = int(input())
divlist = []
ans = 100000
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        divlist.append(i)
for i in divlist:
    fa = len(str(i))
    fb = len(str(int(n / i)))
    ans = min(ans, max(fa, fb))
print(ans)
