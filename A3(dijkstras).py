# dijkstra algorithm

import heapq

def dijkstra(graph,start):
    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    queue = [(0,start)]

    while(queue):
        cost,node = heapq.heappop(queue)
        for neighbour , weight in graph[node]:
            distance = cost + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(queue,(distance,neighbour))
    return distances
    
graph = {}

def add_edge(u,v,w):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v,w))
    graph[v].append((u,w))

edges = int(input("Enter the no of edges : "))
print("Enter Edges like a b 2")
for _ in range(edges):
    u,v,w = input().split()
    add_edge(u,v,int(w))

start = input("Enter the starting node : ")
print(dijkstra(graph,start))

