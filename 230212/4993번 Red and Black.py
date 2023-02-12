import sys
input = sys.stdin.readline
from collections import deque

while True:
    N,M = map(int,input().rstrip().split()) # N은 가로 M은 세로
    if N==0 and M==0:
        break
    graph = [list(map(str,input())) for _ in range(M)]

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    def bfs(y,x):
        q = deque()
        q.append((y,x))
        cnt = 1 # 시작 지점부터 카운팅 1 디폴트
        
        while q:
            y,x = q.popleft()
            for i in range(4):
                ny = y+dy[i]
                nx = x+dx[i]
                if 0<=ny<M and 0<=nx<N:
                    if graph[ny][nx] == '.':
                        graph[ny][nx] = -1
                        cnt+=1
                        q.append((ny,nx))
                        
        return cnt
                

    for col in range(M):
        for row in range(N):
            if graph[col][row] == '@':
                result = bfs(col,row)
                
    print(result)
