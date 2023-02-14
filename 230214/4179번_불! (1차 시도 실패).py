# 틀렸지만 자력으로 많이 끌어올렸던 문제
# 앞서 보물섬 / 치즈를 풀면서 깨달은 스킬을 잘 적용은 했다
# 다만, 엣지케이스들을 많이 고려하지 않아서 조건을 몇개 더 추가해놔야하는 코드
# 이제 엣지케이스들도 고려해서 1트에 패스할 수 있도록 해봐야겠다. 로직은 이대로 갈 예정이다.

from collections import deque
import sys
sys.stdin = open("test.txt")

N,M = map(int,input().split()) # N은 세로 M은 가로
graph = [list(input()) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

q = deque()

def bfs():
    flag = 0
    while q:
        if flag == 1:
            break
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if visited[ny][nx] == 0 and graph[ny][nx] == '.':
                    if ny==N-1 or ny==0 or nx==M-1 or nx==0:
                        visited[ny][nx] = visited[y][x]+1
                        max_check = visited[ny][nx]
                        flag = 1
                        break
                    else:
                        visited[ny][nx] = visited[y][x]+1
                        q.append((ny,nx))
    
    return max_check+1

for col in range(N):
    for row in range(M):
        if graph[col][row] == 'J':
            q.append((col,row))
            visited = [[0]*M for _ in range(N)]
            visited[col][row] = 0
            result = bfs()

for col in range(N):
    for row in range(M):
        if graph[col][row] == 'F':
            q.append((col,row))
            visited = [[0]*M for _ in range(N)]
            visited[col][row] = 0           
            result2 = bfs()

if result>=result2:
    print(result)

else:
    print("IMPOSSIBLE")
