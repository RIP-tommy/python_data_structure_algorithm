import sys

input = sys.stdin.readline

T = int(input())

tree = dict()

for i in range(T):
    a, b, c = input().rstrip().split()
    tree[a] = [b, c]


def in_ord(t):
    keys = list(t.keys())
    current = keys[0]
    count = 0
    visited = list()
    while current != keys[-1]:
        print(keys[i])
        visited.append(keys[i])
        if t[keys[i]][0] != '.':
            current = t[keys[i]][0]
        else:
            current = t[keys[i]][0]

in_ord(tree)