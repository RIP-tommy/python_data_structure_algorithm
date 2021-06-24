import sys
from queue import Queue

input = sys.stdin.readline

n = 0

a, b, c = map(int, input().rstrip().split())

graph = {}

for id in range(a):
    graph[id + 1] = list()

while(n != b):
    d, e = map(int, input().rstrip().split())
    graph[d].append(e)
    graph[e].append(d)
    n+=1

for id in range(a):
    graph[id + 1].sort()

def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            print(node, end=' ')
            stack.extend(reversed(graph[node]))

    print()

def bfs(graph, start_node):
    visit = set()
    q = Queue()

    q.put(start_node)

    while q.qsize() > 0:
        node = q.get()
        if node not in visit:
            visit.add(node)
            print(node, end=' ')            
            for nextNode in graph[node]:
                q.put(nextNode)

    print()
