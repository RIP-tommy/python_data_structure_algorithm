import sys
input = sys.stdin.readline

house_n = int(input())

n = 0

map_info = list()

while(n != house_n):
    map_info.append(input().rstrip())
    n+=1

def dfs(map_info):
    visit = list()
    stack = list()

    stack.append([0, 0])

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(reversed(map_info[node]))
