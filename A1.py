# bfs and dfs
graph = {}

def add_edge(u,v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

def dfs(node,visited):
    visited.append(node)
    print(node,end=' ')
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour,visited)

def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        node = queue.pop(0)
        print(node,end=' ')
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

edges = int(input("Enter the no of edges: "))
print("Enter the edges like a b : ")
for _ in range(edges):
    u,v = input().split()
    add_edge(u,v)

start = input("\nEnter starting node")
print("\ndfs")
dfs(start,[])
print("\nbfs")
bfs(start)