#https://atcoder.jp/contests/abc122/tasks/abc122_b
s = input()
l = ['A', 'T', 'G', 'C']
n = len(s)
num = 0
ans = 0
# sの文字列について一文字目から見ていく
for i in range(n):
    if s[i] in l:
        num += 1
    else:
        # ansの更新
        # numのリセット
        ans = max(num, ans)
        num = 0
# 最後の一つが'A','T','G','C'だった時用
ans = max(num, ans)
