a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# n = 20の時点で既に動きが怪しい
def rec(i, maxsum):
    if i == n:
        return maxsum
    newsum = max(rec(i + 1, maxsum), rec(i + 1, maxsum + a[i]))
    return newsum
n = 20
print(rec(0, 0))
