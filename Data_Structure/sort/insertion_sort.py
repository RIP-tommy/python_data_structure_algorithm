import random

arr = [i for i in range(0, 100, random.randint(1, 31))]

random.shuffle(arr)

print(arr)

for i in range(1, len(arr)):
    n = 0
    while i - n > 0:
        if arr[i - n] < arr[i - n - 1]:
            temp = arr[i - n - 1]
            arr[i - n - 1] = arr[i - n]
            arr[i - n] = temp
        n += 1

print(arr)