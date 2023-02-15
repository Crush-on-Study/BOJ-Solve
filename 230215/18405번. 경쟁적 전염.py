from collections import deque

N,K = map(int,input().split())
# arr_K = [i for i in range(1,K+1)]

graph,virus = [],[]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for col in range(N):
    graph.append(list(map(int,input().split())))
    for row in range(N):
        if graph[col][row] != 0:
            virus.append((graph[col][row],0,col,row)) # 바이러스 , 시간, 좌표

virus.sort()
q = deque(virus)

t,yy,xx = map(int,input().split())

def bfs():
    while q:
        data,time,y,x = q.popleft() # 바이러스, 시간, 좌표
        if time==t: # 시간이 오면
            break

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<N:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = data
                    q.append((data,time+1,ny,nx))

    return graph[yy-1][xx-1]

print(bfs())
