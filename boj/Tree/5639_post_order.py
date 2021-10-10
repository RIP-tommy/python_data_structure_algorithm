import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def print_node(start, end):
    if start > end:
        return
    
    root = tree[start] 
    idx = start + 1

    while idx <= end:
        if tree[idx] > root:
            break
        idx += 1

    print_node(start + 1, idx - 1)
    print_node(idx, end)
    print(root)

tree = list()

while True:
    try:
        tree.append(int(input()))
    except:
        break

print_node(0, len(tree) - 1)