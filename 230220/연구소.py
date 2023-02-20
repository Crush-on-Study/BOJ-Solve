from collections import deque

N,M = map(int,input().split()) # N은 세로요 M은 가로입니다
graph = [list(map(int,input().split())) for _ in range(N)]
wall = [[0]*M for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def bfs(y,x):
    q = deque()
    q.append((y,x))

    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if not wall[ny][nx]:
                    wall[ny][nx] = 2
                    q.append((ny,nx))

def cnt0():
    ccnt=0
    for col in range(N):
        for row in range(M):
            if wall[col][row] == 0:
                ccnt+=1

    return ccnt

max_check = -100

def dfs(cnt):
    global max_check
    if cnt==3:
        for col in range(N):
            for row in range(M):
                wall[col][row] = graph[col][row] # 앙 기모기모기모링
    
        for col in range(N):
            for row in range(M):
                if wall[col][row] == 2:
                    bfs(col,row)
                    
        max_check = max(max_check,cnt0())
        return

    for col in range(N):
        for row in range(M):
            if graph[col][row] == 0:
                graph[col][row] = 1 # 벽 설치요옷
                cnt+=1
                dfs(cnt)
                graph[col][row] = 0
                cnt-=1

dfs(0)
print(max_check)
