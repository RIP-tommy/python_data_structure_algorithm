def selection_sort(arr):
    s_a = list()
    for i in range(len(arr)):
        s_a.append(min(arr))
        del arr[arr.index(min(arr))]
    return s_a