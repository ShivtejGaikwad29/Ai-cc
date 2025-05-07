# a star algorithm
import heapq

def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(grid,start,goal):
    rows,cols = len(grid) , len(grid[0])
    visited = set()
    open_list = [(0+heuristic(start,goal),0,start,[])]

    while(open_list):
        f,g,current,path = heapq.heappop(open_list)

        if current in visited:
            continue
        visited.add(current)
        path = path+[current]

        if current == goal:
            return path
        
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = current[0]+dx , current[1]+dy
            if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==0:
                neighbour = (nx,ny)
                if neighbour not in visited:
                    heapq.heappush(open_list,(g+1+heuristic(current,goal),g+1,neighbour,path))
    return None

grid = eval(input("Enter the grid like [[1,2,3,4],[5,6,7,8]].. : "))
print("grid entered : ")
for row in grid:
    print(row)

start = eval(input("Enter the start state like (0,0) : "))
goal = eval(input("Enter the Goal state like (1,5) : "))

path = astar(grid,start,goal)
if path:
    for p in path:
        print(p)
else:
    print("No path found")

