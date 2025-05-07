# kruskal algortihm

def find(parent,node):
    if(parent[node]==node):
        return node
    return find(parent,parent[node])

def union(parent,u,v):
    root_u = find(parent,u)
    root_v = find(parent,v)

    if(root_u != root_v):
        parent[root_v] = root_u
        return True
    return False

def kruskal(vertices,edges):
    edges.sort(key = lambda x:x[2])
    mst = []
    total_cost = 0
    parent = {v : v for v in vertices}

    for u,v,w in edges:
        if(union(parent,u,v)):
            mst.append((u,v,w))
            total_cost += w
    return mst,total_cost

vertices = []
edges = []

vcount = int(input("Enter the number of vertices : "))
print("Enter the edge like a b c : ")
for _ in range(vcount):
    vertices.append(input().strip())


ecount = int(input("Enter the number of edges : "))
print("Enter the edge like a b 2 : ")
for _ in range(ecount):
    u,v,w = input().split()
    edges.append((u,v,int(w)))

mst , cost = kruskal(vertices,edges)
print("cost",cost)
for r in mst:
    print(r)