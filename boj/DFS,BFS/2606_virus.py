import sys
input = sys.stdin.readline

pc_n = int(input())
pair = int(input())

n = 0

graph = [[] for __ in range(pc_n + 1)]

while(n != pair):
    d, e = map(int, input().rstrip().split())
    graph[d].append(e)
    graph[e].append(d)
    n+=1

def dfs(graph):
    visit = list()
    stack = list()

    stack.append(1)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(reversed(graph[node]))

    visit.pop(0)

    return visit

ans = dfs(graph)

print(len(ans))