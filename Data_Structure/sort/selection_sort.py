import random

arr = [i for i in range(0, 100, random.randint(1, 31))]

random.shuffle(arr)

print(arr)

s_a = list()

for i in range(len(arr)):
    s_a.append(min(arr))
    del arr[arr.index(min(arr))]

print(s_a)