from collections import deque

N,M = map(int,input().split())
graph = [list(input()) for _ in range(N)]

fvisited = [[0]*M for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]


jvisited = [[0]*M for _ in range(N)]

fq = deque()
jq = deque()

def bfs():
    while fq:
        y,x = fq.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if fvisited[ny][nx] == 0 and graph[ny][nx] == '.':
                    fvisited[ny][nx] = fvisited[y][x]+1
                    fq.append((ny,nx))
    
    while jq:
        y,x = jq.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if jvisited[ny][nx] == 0 and graph[ny][nx] == '.':
                    if not fvisited[ny][nx] or fvisited[ny][nx] > jvisited[y][x]+1: # 불 이동경로랑 비교했을 때
                        jvisited[ny][nx] = jvisited[y][x]+1
                        jq.append((ny,nx))
            
            else:
                return jvisited[y][x]+1
    
    return "IMPOSSIBLE"
    

for col in range(N):
    for row in range(M):
        if graph[col][row] == 'F':
            fq.append((col,row))
        elif graph[col][row] == 'J':
            jq.append((col,row))

print(bfs())
