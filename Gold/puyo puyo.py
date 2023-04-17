import sys
from collections import deque

dx,dy = [1,0,-1,0],[0,1,0,-1]

graph = []
for _ in range(12):
    graph.append(list(map(str,input())))

result = 0

def bfs(y,x,color):
    q = deque()
    q.append((y,x))
    
    visited = [[False]*6 for _ in range(12)]
    visited[y][x] = True
    block = [(y,x)]
    cnt = 1
    
    flag = 0
    
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<12 and 0<=nx<6 and not visited[ny][nx] and graph[ny][nx] == color:
                visited[ny][nx] = True
                cnt +=1
                q.append((ny,nx))
                block.append((ny,nx))
                    
    if cnt >= 4:
        flag = 1
        
        for idx in block:
            y,x = idx
            graph[y][x] = '.'
    
    return flag
        
            
def gravity():
    for col in range(6):
        for row in range(0,12)[::-1]:
            if graph[row][col] != '.':
                for k in range(row+1,13):
                    if k==12 or graph[k][col] != '.':
                        graph[row][col],graph[k-1][col] = graph[k-1][col],graph[row][col]
                        break

while True:
    point = 0
    for col in range(12):
        for row in range(6):
            if graph[col][row] != '.':
                color = graph[col][row]
                point += bfs(col,row,color)
    
    if point == False:
        print(result)
        break
    
    else:
        result += 1
    
    gravity()
