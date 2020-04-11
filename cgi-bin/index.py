import itertools
n, m = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))

cnt = 0
# 複数の集合から要素を一つずつ取り出した時の組み合わせの集合
# スイッチの全ての組み合わせ
for bits in itertools.product([0, 1], repeat = n):
    # 電球を並べる
    lights = [0] * m

    for i in range(n):
        # もしスイッチがONなら
        if bits[i] == 0:
            sw = i + 1
            for j in range(len(ks)):
                if sw in ks[j][1:]:
                    # そのスイッチが関係する電球にプラス１
                    lights[j] += 1
    m_lighs = [l % 2 for l in lights]
    if m_lights == p:
        cnt += 1
print(cnt)
