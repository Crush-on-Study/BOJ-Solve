N,M,T = map(int,input().split())

dx,dy = [1,0,-1,0],[0,1,0,-1]
graph = []
for col in range(N):
    graph.append(list(map(int,input().split())))

wind = []
for col in range(N):
    for row in range(M):
        if graph[col][row] == -1:
            wind.append((col,row))

new_graph = [[0]*M for _ in range(N)]

#### 1번 행동 확산 (완료 : 디버깅 노필요) ####
def spread(graph):
    for y in range(N):
        for x in range(M):
            if graph[y][x] != -1:
                cnt = 0
                for i in range(4):
                    ny = y+dy[i]
                    nx = x+dx[i]
                    if 0<=ny<N and 0<=nx<M:
                        if graph[ny][nx] != -1:
                            cnt+=1
                            new_graph[ny][nx] += graph[y][x] // 5
            
                new_graph[y][x] += graph[y][x] - (graph[y][x]//5)*cnt
    
    new_graph[wind[0][0]][wind[0][1]] = -1
    new_graph[wind[1][0]][wind[1][1]] = -1

    return new_graph

def clean(new_graph):
    new2_graph = [[0]*M for _ in range(N)]
    up_y,up_x = wind[0]
    down_y,down_x = wind[1]

    # 상단, 하변  왼 -> 오
    for idx in range(2,M):
        new2_graph[up_y][idx] = new_graph[up_y][idx-1]

    # 상단, 우변  아래 -> 위
    for idx in range(up_y,-1,-1):
        new2_graph[idx-1][M-1] = new_graph[idx][M-1]
        # for jdx in range(1,M):
        #     new2_graph[idx][jdx] = new_graph[idx][jdx]
    
    # 상단, 위쪽  오 -> 왼
    for idx in range(1,M):
        new2_graph[0][idx-1] = new_graph[0][idx]

    # 상단, 좌변 위 -> 아래
    for idx in range(1,up_y+1):
        new2_graph[idx][0] = new_graph[idx-1][0]
    new_graph[up_y][0] = 0
    new2_graph[up_y][0] = 0
#################################################
    # 하단, 윗변  왼 -> 오
    for idx in range(2,M):
        new2_graph[down_y][idx] = new_graph[down_y][idx-1]

    # 하단, 우변  위 -> 아래
    for idx in range(down_y+1,N):
        new2_graph[idx][M-1] = new_graph[idx-1][M-1]

    # 하단, 아랫변 오 -> 왼
    for idx in range(1,M):
        new2_graph[N-1][idx-1] = new_graph[N-1][idx]

    # 하단, 좌변 아래 -> 위
    for idx in range(N-1,down_y,-1):
        new2_graph[idx-1][0] = new_graph[idx][0]
    new_graph[down_y][0] = 0
    new2_graph[down_y][0] = 0
        

##########################################

    # new2_graph[up_y][up_x] = -1
    # new2_graph[down_y][down_x] = -1

    for idx in range(1,up_y):
        for jdx in range(1,M-1):
            new2_graph[idx][jdx] = new_graph[idx][jdx]

    for idx in range(down_y+1,N-1):
        for jdx in range(down_x+1,M-1):
            new2_graph[idx][jdx] = new_graph[idx][jdx]

    return new2_graph


for _ in range(T):
    mid = spread(graph)
    graph = clean(mid)

for col in graph:
    print(col)

tot = 0
for col in graph:
    tot+=sum(col)

print(tot)
