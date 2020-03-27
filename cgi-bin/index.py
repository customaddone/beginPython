#2の累乗でもっとも大きいものをansに
#2,4,8と試していく
n = int(input())
ans = 1
for i in range(7):
    if 2**i<=n:ans=a**i
print(ans)
