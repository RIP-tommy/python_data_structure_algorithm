import sys
input = sys.stdin.readline

T = int(input())

stack = list()

for ord in range(0, T):
    n = input().split()
    if n[0] == "push":
        stack.append(int(n[1]))
    if n[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            out = stack.pop()
            print(out)
    elif n[0] == "size":
        print(len(stack))
    elif n[0] == "empty":
        if len(stack) == 0:
            print(1)
        else: 
            print(0)
    elif n[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
