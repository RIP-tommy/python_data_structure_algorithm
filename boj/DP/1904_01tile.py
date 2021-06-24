import sys
input = sys.stdin.readline

res = [0 for _ in range(1, 1000000)]

res[1] = 1
res[2] = 2

for i in range(2, 1000000):
    res[i] = res[i - 1] + res[i - 2]

T = int(input())
print(res[T]%15746)