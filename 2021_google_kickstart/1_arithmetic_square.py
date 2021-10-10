import sys
input = sys.stdin.readline

T = int(input())

TC = [[[], [], []] for __ in range(T)]

for i in range(T):
    for j in range(3):
        if j != 1:
            a, b, c = map(int, input().rstrip().split())
            TC[i][j].append(a)
            TC[i][j].append(b)
            TC[i][j].append(c)
        else:
            a, b = map(int, input().rstrip().split())
            TC[i][j].append(a)
            TC[i][j].append(0)
            TC[i][j].append(b)


def solve(case):
    print(case)


for i in range(T):
    solve(TC[i])
