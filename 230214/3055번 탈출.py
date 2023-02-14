from collections import deque

N,M = map(int,input().split()) # N은 세로 M은 가로
graph = [list(input()) for _ in range(N)] # 그래프

gosu = deque() # 고슴도치도치
water = deque()

gvisited = [[0]*M for _ in range(N)]
wvisited = [[0]*M for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs():
    while water:
        y,x = water.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M: # 범위 안벗어났고
                if not wvisited[ny][nx] and graph[ny][nx] == '.': # 물이 아직 닿지 않은 곳이며 이동 가능한 곳이면
                    wvisited[ny][nx] = wvisited[y][x]+1 # 카운팅 ㄱㄱ
                    water.append((ny,nx))
    
    
    while gosu:
        y,x = gosu.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if not gvisited[ny][nx] and graph[ny][nx] == '.':
                    if not wvisited[ny][nx] or wvisited[ny][nx] > gvisited[y][x]+1:
                        gvisited[ny][nx] = gvisited[y][x]+1
                        gosu.append((ny,nx))
            
                elif not gvisited[ny][nx] and graph[ny][nx] == 'D':
                    return gvisited[y][x]+1
    
    return "KAKTUS"                


for col in range(N):
    for row in range(M):
        if graph[col][row] == '*': # 고슴도치니?
            water.append((col,row)) # 큐에 넣고
        
        elif graph[col][row] == 'S': # 물이니?
            gosu.append((col,row))
            
print(bfs())
