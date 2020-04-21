lista = [i for i in range(10)]

def binary_search_loop(data, target):
    imin = 0
    imax = len(data) - 1
    while imin <= imax:
        imid = imin + (imax - imin) // 2
        if target == data[imid]:
            return imid
        elif target < data[imid]:
            imax = imid - 1
        else:
            imin = imid + 1
    return False
print(binary_search_loop(lista, 10))
