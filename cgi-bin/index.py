N=int(input())
S=input()
# ord 文字 →　アスキーコード
# chr アスキーコード → 文字
# 大文字のAは６５番、小文字のaは９７番
# Z → Aへとループさせるために%26する
print("".join(chr(65+(ord(s)-65+N)%26) for s in S))
