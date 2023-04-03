from collections import deque
import sys
sys.stdin = open('test.txt')
# N은 격자 사이즈, M은 사람 수
N,M = map(int,input().split())

# 그래프 정보 / 베이스캠프 위치
graph = []
basecamp = deque()
for col in range(N):
    graph.append(list(map(int,input().split())))
    for row in range(N):
        if graph[col][row] == 1:
            basecamp.append((col,row))

cu_info = []
for col in range(M):
    # 편의점 위치
    y,x = map(int,input().split())
    cu_info.append((y-1,x-1))

dx,dy = [1,0,-1,0],[0,1,0,-1]

########### 세팅 끝 ##############
def bfs(y,x):
    visited = [[-1]*N for _ in range(N)]
    q = deque()
    q.append((y,x))
    visited[y][x] = 0

    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<N:
                if visited[ny][nx] == -1 and graph[ny][nx] != -100:
                    visited[ny][nx] = visited[y][x]+1
                    q.append((ny,nx))
    
    return visited


################################
time = 0
cnt = 1
for idx in basecamp:
    y,x = idx # 베이스캠프의 위치 스으윽 나와주고
    result = bfs(y,x)    
    
    print(f"{cnt}번째 방문 경로 그래프")
    for col in result:
        print(col)
    
    """
    [1, 2, 3, 4, 5]
    [0, 1, 2, 3, 4]
    [1, 2, 3, 4, 5]
    [2, 3, 4, 5, 6]
    [3, 4, 5, 6, 7]
    """
    arr = [] # 현재 베이스캠프에서의 모든 편의점과의 거리
    for k in cu_info:
        cy,cx = k
        arr.append((result[cy][cx],cy,cx))

    # 최단거리, 세로, 가로
    arr = sorted(arr,key=lambda x : (x[0],x[1],x[2]))
    """
    # 쏘트 전
    [(2, 1, 2), (5, 3, 3), (3, 4, 0)]
    [(2, 1, 2), (3, 3, 3), (7, 4, 0)]
    [(3, 1, 2), (2, 3, 3), (2, 4, 0)]
    [(5, 1, 2), (2, 3, 3), (4, 4, 0)]

    # 쏘트 후
    [(2, 1, 2), (3, 4, 0), (5, 3, 3)]
    [(2, 1, 2), (3, 3, 3), (7, 4, 0)]
    [(2, 3, 3), (2, 4, 0), (3, 1, 2)]
    [(2, 3, 3), (4, 4, 0), (5, 1, 2)]
    """
    if arr:
        # 현재 위치에서의 거리, 편의점 위치
        dis,fy,fx = arr.pop(0)        
        time+=dis
        graph[fy][fx] = -100

    print(f"{cnt}번째 그래프")
    for col in graph:
        print(col)

    cnt+=1

print(time)
