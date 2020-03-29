# 二分探索
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def binary_search(list, x):
    low = 0
    high = len(list)

    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return None
print(binary_search(a, 9))
