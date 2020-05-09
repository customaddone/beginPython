# https://atcoder.jp/contests/abc122/tasks/abc122_b
# 最も長いACGT文字列の長さを求める →　前から条件についてジャッジして、NGなら0にする
# 最長共通部分列、最長増加部分列が思い浮かぶ
# 前から条件についてジャッジして、NGなら0にする
s = input()
l = ['A', 'T', 'G', 'C']
n = len(s)
# 現在の長さ
num = 0
# 一番の長さ
ans = 0
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
print(ans)
