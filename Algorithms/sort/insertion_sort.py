def insertion_sort(arr):
    for i in range(1, len(arr)):
        n = 0
        while i - n > 0:
            if arr[i - n] < arr[i - n - 1]:
                temp = arr[i - n - 1]
                arr[i - n - 1] = arr[i - n]
                arr[i - n] = temp
            n += 1


# 책에 있는 코드입니다.

# from typing import MutableSequence

# def insertion_sort(a: MutableSequence) -> None:
#     """단순 삽입 정렬"""
#     n = len(a)
#     for i in range(1, n):
#         j = i
#         tmp = a[i]
#         while j > 0 and a[j - 1] > tmp:
#             a[j] = a[j - 1]
#             j -= 1
#         a[j] = tmp

# insertion_sort(arr)

# print(arr)
