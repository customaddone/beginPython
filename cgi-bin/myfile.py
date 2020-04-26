n = 8

def check(x, col):
    for i, row in enumerate(reversed(col)):
        # 0 + 1個左、1 + 1個左...
        if (x + (i + 1) == row) or (x - (i + 1) == row):
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
                col.pop()
search([])
