import sys
input = sys.stdin.readline

res = [0 for _ in range(101)]
res[0] = 0
res[1] = 1
res[2] = 1
res[3] = 1
res[4] = 2
res[5] = 2
res[6] = 3
res[7] = 4
res[8] = 5
res[9] = 7
res[10] = 9

for i in range(11, 101):
    res[i] = res[i - 1] + res[i -5]

T = int(input())
for i in range(T):
    n = int(input())
    print(res[n])