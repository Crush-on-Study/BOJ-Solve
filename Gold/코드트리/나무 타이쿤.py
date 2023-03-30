# 세로, 가로
N,M = map(int,input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

#    → ↗ ↑ ↖ ← ↙ ↓ ↘
dx = [1,1,0,-1,-1,-1,0,1] 
dy = [0,-1,-1,-1,0,1,1,1]

cloud = [[N-2,0],[N-2,1],
        [N-1,0],[N-1,1]]

info = []
for _ in range(M):
    d,p = map(int,input().split()) # d는 이동 방향 , p는 이동 칸 수
    info.append((d-1,p))

for tc in range(M):
    new_cloud = []
    d,p = info[tc]    
    # 1번 행동 시작
    for idx in cloud:
        y,x = idx
        
        ny = (y+dy[d]*p)%N
        nx = (x+dx[d]*p)%N
        new_cloud.append((ny,nx))

    # 2번 행동 시작
    visited = [[False]*N for _ in range(N)]
    for idx in new_cloud:
        y,x = idx
        graph[y][x]+=1
        visited[y][x] = True # 특수 영양제 맞은 곳 방문처리
    
    # 비워주고
    cloud = []

    # 3번 행동 시작 (영양제 박기)
    for idx in new_cloud:
        cnt = 0
        y,x = idx

        cx = [1,1,-1,-1]
        cy = [1,-1,1,-1]
        for i in range(4):
            ny = y+cy[i]
            nx = x+cx[i]
            # 격자 벗어나면 안된다.
            if 0<=ny<N and 0<=nx<N:
                if graph[ny][nx] > 0:
                    cnt+=1 # 카운팅 해주고

        graph[y][x] += cnt

    # 4번 행동 높이 2 이상인 곳 커트
    for col in range(N):
        for row in range(N):
            if visited[col][row] == False: # 방문 안했고
                if graph[col][row] >= 2: # 2 이상인 곳
                    graph[col][row]-=2
                    cloud.append((col,row))


tot = 0
for col in range(N):
    for row in range(N):
        tot+=graph[col][row]

print(tot)
