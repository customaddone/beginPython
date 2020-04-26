n = 8

def check(x, col):
    for i in range(len(col)):
        # 0 + 1個左、1 + 1個左...
        # range()[::-1]はインデックスも逆になる
        # col[-1]はcolの後ろから1つ目
        if (x + (i + 1) == col[-1 * i - 1]) or (x - (i + 1) == col[-1 * i - 1]):
            return False
    return True

def search(col):
    # 全て配置したら終了
    if len(col) == n:
        print(col)
    for i in range(n):
        # 同じ行は使わない
        if i not in col:
            # もし斜めチェックがOKなら
            if check(i, col):
                col.append(i)
                search(col)
                # ダメなら元に戻す
                col.pop()
search([])
