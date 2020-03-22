l, r = map(int, input().split())
ans = 0
min2019 = 2019 * (l // 2019)
max2019 = 2019 * ((r // 2019) + 1)
if r < (min2019 + 2019):
    absvalue = min((l - min2019), (max2019 - r))
    ans = absvalue * (absvalue + 1)
print(ans)
