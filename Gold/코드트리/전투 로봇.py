import sys
from collections import deque
sys.stdin = open('111.txt')

input = sys.stdin.readline

N = int(input().rstrip())
graph = []
for col in range(N):
    graph.append(list(map(int,input().rstrip().split())))
    for row in range(N):
        if graph[col][row] == 9:
            sy,sx = col,row # 상어 위치 저장
            graph[col][row] = 0
    

q = deque()


dx,dy = [1,0,-1,0],[0,1,0,-1]
shark_size = 2

# 물고기 찾으러 감
def search():
    visited = [[-1]*N for _ in range(N)]
    visited[sy][sx] = 0 # 상어 시작 위치
    q.append((sy,sx))
    
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<N:
                if visited[ny][nx] == -1:
                    if -1<=graph[ny][nx] <= shark_size:
                        visited[ny][nx] = visited[y][x]+1
                        q.append((ny,nx))
                        
    return visited


def eating(visited):
    min_check = int(1e9)
    for col in range(N):
        for row in range(N):
            if 1<=graph[col][row] < shark_size:
                if visited[col][row] != -1:
                    if visited[col][row] < min_check:
                        min_check = visited[col][row]
                        sy,sx = col,row
                        
    if min_check == int(1e9):
        return False # 더 이상 먹을게 없다는 뜻
    
    return sy,sx,min_check

time = 0
eat_cnt = 0 # 물고기 먹은 횟수
while True:
    visited = search()    
    result = eating(visited)
    
    if result == False:
        print(time)
        break
    
    sy,sx = result[0],result[1] # 상어 재 시작 위치
    time += result[2]
    graph[sy][sx] = 0
    eat_cnt += 1
    
    if eat_cnt >= shark_size:
        shark_size+=1
        eat_cnt = 0 
