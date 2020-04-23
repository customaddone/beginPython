import math
def make_divisors(m, n):
    divisors = []
    numi = min(m, n)
    numa = max(m, n)
    for i in range(1, int(math.sqrt(numi)) + 1):
        if numi % i == 0:
            if numa % i == 0:
                divisors.append(i)
            # √nで無い数についてもう一個プラス
            if i != numi // i and numa % (numi // i) == 0:
                divisors.append(numi // i)
    return sorted(divisors)
print(make_divisors(13, 19))
