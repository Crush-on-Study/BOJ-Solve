from collections import deque

N,M = map(int,input().split()) # N은 세로 M은 가로
graph = [list(map(int,input().split())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
cnt = 0

def outside(): # 가장 위
    for row in range(M):
        graph[0][row] = -1

def outside2(): # 가장 아래
    for row in range(M):
        graph[N-1][row] = -1

def outside3(): # 가장 좌측
    for col in range(N):
        graph[col][0] = -1

def outside4(): # 가장 우측
    for col in range(N):
        graph[col][M-1] = -1

outside()
outside2()
outside3()
outside4()

def contamination(y,x): # 외부공기를 전부 -1로 처리해버림
    q = deque()
    q.append((y,x))
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = -1
                    q.append((ny,nx))

    return graph

for col in range(N):
    for row in range(M):
        if graph[col][row] == -1:
            new_graph = contamination(col,row)


# for col in range(N):
#     print(new_graph[col])

##################################################

def search(y,x):
    tot = N*M
    global cnt

    while tot!=0:
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if new_graph[ny][nx] == -1: # 이부분 어떻게 가변적이게 할까.?
                  new_graph[y][x] = 2 # 이부분 어떻게 카운팅할까..?
                    cnt+=1
        tot-=1
    return new_graph

arr = []

for col in range(N):
    for row in range(M):
        if new_graph[col][row] == 1:
            cnt = 1
            z = search(col,row)
         

for col in range(N):
    print(z[col])

# print(arr)

# 아이디어
# 가장 바깥 쪽들을 -1로 처리한 뒤, 그걸 기점으로 bfs를 시도했다.
# 그렇게 바깥공기를 모두 -1로 처리하였고  이제 -1과 맞닿은 1들을 카운팅해서 2,3,... 이런 식으로 가도록하고자 했다.
# 근데 여기서 더 어떻게 카운팅해야할지 막혔다
