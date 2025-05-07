# prims algorithm

import heapq

def primsalgo(graph,start):
    visited = set()
    min_heap = [(0,start)]
    mst_count = 0

    while(min_heap):
        cost,node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            mst_count += cost
        for neighbour,weight in graph[node]:
            if neighbour not in visited:
                heapq.heappush(min_heap,(weight,neighbour))
    return mst_count

graph = {}
def add_edge(u,v,w):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v,w))
    graph[v].append((u,w))

edge = int(input("Enter the number of edges : "))
print("Enter the edge like A B 4")
for _ in range(edge):
    u,v,w = input().split()
    add_edge(u,v,int(w))

start = input("Enter the start node : ")

print(primsalgo(graph,start))

