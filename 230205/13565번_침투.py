# 베이직한 경로탐색 문제
# BFS를 사용했고 위쪽 경계와 아랫쪽 경계에 하나라도 True가 있으면 연결된 것으로 판단함

import sys
input = sys.stdin.readline
from collections import deque
N,M = map(int,input().rstrip().split())

graph = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

step = [(1,0),(-1,0),(0,1),(0,-1)] # 4방향 스텝
cnt = 1
def bfs(y,x):
    global cnt
    q = deque()
    q.append((y,x))
    
    while q:
        y,x = q.popleft()
        for i in step:
            ny = y+i[0]
            nx = x+i[1]
            if 0<=ny<N and 0<=nx<M:
                if visited[ny][nx] == False and graph[ny][nx] == 0:
                    visited[ny][nx] = True
                    cnt+=1
                    q.append((ny,nx))
    return visited

tot = 0

for col in range(1): # 맨 윗줄만 보면 된다~
    for row in range(M):
        if visited[col][row] == False and graph[col][row]==0:
            visited[col][row] = True
            cnt = 1 # 초기화
            a = (bfs(col,row))
            tot += sum(a[N-1])  # 불리안 연산을 통해 0이면 연결 X, 0이상이면 연결 O로 판단

if tot>0:
    print("YES")
    
else:
    print("NO")
    
# 가장 간단한 그래프탐색 이론이므로 이런 문제는 한번에 맞추지못하면 심각하다~
