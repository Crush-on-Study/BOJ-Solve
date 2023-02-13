# 어차피 2중 포문으로 모든 곳을 탐색하니까 상관없다. 
# 간단한 문제였음 max값만 잘쓰면 된다
from collections import deque

N,M = map(int,input().split()) # N은 세로 M은 가로
graph = [list(input()) for _ in range(N)] # 그래프정보 입력받고

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(y,x):
    q = deque()
    q.append((y,x))
    visited = [[0]*M for _ in range(N)]
    visited[y][x] = 1 # 방문처리해주고
    cnt = 0
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if graph[ny][nx] == 'L' and not visited[ny][nx]:
                    visited[ny][nx] = visited[y][x]+1
                    cnt = max(cnt,visited[ny][nx]) # 이게 의미가 뭘까?
                    q.append((ny,nx))

    return cnt-1

result = 0
for col in range(N):
    for row in range(M):
        if graph[col][row] == 'L': # 육지면
            a = bfs(col,row)
            result = max(result,a)

print(result)
