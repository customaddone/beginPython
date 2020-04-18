def binary_search_loop(data,target):
    imin = 0
    imax = len(data) - 1
    while imin <= imax:
        imid = imin + (imax + imin) // 2
        if target == data[imid]:
            return True
        elif target < data[imid]:
            imax = imid - 1
        else:
            imin = imid + 1
    return False
