# 辞書順でどちらが早いかは<でできる
a, b = input().split()
print(a*int(b) if a<b else b*int(a))
