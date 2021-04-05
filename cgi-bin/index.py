S = 'atcoder'
K = 3

N = len(S)
L = [[] for i in range(26)]
for i in range(N - 1, -1, -1):
    L[ord(S[i]) - ord('a')].append(i)

#  現在選択し終えた文字列のうち最新の文字
now = -1
ans = ''
# k文字目に何を選ぶか
for k in range(K):
    # a ~ zについて探索する
    for j in range(26):
        # 現在の文字より前にあるものは全て取り除く
        while L[j] and L[j][-1] <= now:
            L[j].pop()
        # N - L[j][-1]: この文字を含めたSの残りの文字数
        # K - k: 指定する必要のある残りの文字数
        if L[j] and N - L[j][-1] >= K - k:
            now = L[j].pop()
            ans += S[now]
            break

print(ans)
