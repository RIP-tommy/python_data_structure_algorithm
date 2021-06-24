import sys

input = sys.stdin.readline

res = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

for a in range(0, 21):
    for b in range(0, 21):
        for c in range(0, 21):
            if a == 0 or b == 0 or c == 0:
                res[a][b][c] = 1
            elif a < b and b < c:
                res[a][b][c] = res[a][b][c-1] + res[a][b-1][c-1] - res[a][b-1][c]
            else:
                res[a][b][c] = res[a-1][b][c] + res[a-1][b-1][c] + res[a-1][b][c-1] - res[a-1][b-1][c-1]

while(True):
    a, b, c = map(int, input().rstrip().split())
    if a == -1 and b == -1 and c== -1:
        break
    if a <= 0 or b <= 0 or c <= 0:
        print("w(%d, %d, %d) = %d"%(a, b, c, 1))
    elif a > 20 or b > 20 or c > 20:
        print("w(%d, %d, %d) = %d"%(a, b, c, 1048576))
    else:
        print("w(%d, %d, %d) = %d"%(a, b, c, res[a][b][c]))