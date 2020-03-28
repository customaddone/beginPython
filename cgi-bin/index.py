# 1~3文字目,2~4文字目...を順に探索
n = int(input())
s = input()
print(sum(s[i:i+3] == 'ABC' for i in range(N-2)))
