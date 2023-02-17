from collections import deque
N,M = map(int,input().split()) # N은 세로 M은 가로  (1,1부터 시작함) K는 부술수 있는 벽 개수

graph = [list(map(int,input())) for _ in range(N)] # 그래프 정보 쓰아악
visited = [[[0]*2 for _ in range(M)] for _ in range(N)] # 벽 부순 여부까지 포함함
# print(visited)
# q= deque()

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1
    # print(visited)
    while q:
        y,x,z = q.popleft()
        if y==N-1 and x==M-1:
            return visited[y][x][z]

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if visited[ny][nx][z]==0 and graph[ny][nx] == 0: # 미방문했고 지나갈 수 있는 길이라면
                    visited[ny][nx][z] = visited[y][x][z]+1
                    # print(visited)
                    q.append((ny,nx,z))
                
                elif visited[ny][nx][z]==0 and graph[ny][nx] == 1 and z==0: # 벽을 만났는데 부술 기회가 있어!
                    visited[ny][nx][z+1] = visited[y][x][z]+1
                    q.append((ny,nx,z+1))
                
                # z= z+1
    return -1
                    
print(bfs())
