# 변 맞닿은거 세는거에서 막힘. 다들 여기서 막힐듯

from collections import deque
import sys
sys.stdin = open('111.txt')

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

mid = N//2

dx,dy = [1,0,-1,0],[0,1,0,-1]

def bfs(y,x):
    q = deque()
    q.append((y,x))
    num_check = graph[y][x]
    cnt = 1
    differ = 0
    
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<N:
                if graph[ny][nx] == num_check and not visited[ny][nx]:
                    visited[ny][nx] = True
                    cnt += 1
                    q.append((ny,nx))
                    
                elif graph[ny][nx] != num_check and not visited[ny][nx]:
                    differ+=1
    
    return cnt,num_check,differ    
    

def rotate_all():
    new_graph = [[0]*N for _ in range(N)]
    ############# 십자가 ##############
    for idx in range(N):
        new_graph[N-idx-1][mid] = graph[mid][idx]
        
    for idx in range(N):
        new_graph[mid][idx] = graph[idx][mid]


    ########### 정사각형 #############
    # 북서쪽 시계방향
    for col in range(mid):
        for row in range(mid):
            new_graph[row][mid-col-1] = graph[col][row]

    # 북동쪽 시계방향
    for col in range(mid):
        for row in range(mid+1,N):
            new_graph[row-mid-1][N-col-1] = graph[col][row]

    # 남서쪽 시계방향
    for col in range(mid+1,N):
        for row in range(mid):
            new_graph[row-mid][N-col-1] = graph[col][row]

    # 남동쪽 시계 방향
    for col in range(mid+1,N):
        for row in range(mid+1,N):
            new_graph[row][mid-col] = graph[col][row]
            
    
    for col in range(N):
        for row in range(N):
            graph[col][row] = new_graph[col][row]

for _ in range(1):
    arr = []
    visited = [[False]*N for _ in range(N)]
    for col in range(N):
        for row in range(N):
            if visited[col][row] == False:
                visited[col][row] = True
                info = bfs(col,row)
                arr.append(info)
                
    print(arr)
    rotate_all()
