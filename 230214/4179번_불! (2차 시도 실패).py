# 거의 다 왔는데, 현재 처리가 힘든 것 : 지훈이의 이동이 불이나 벽에 막혀 더 이상 이동이 불가할 때도 impossible이 나오게 해야하는데
# 얘 하나를 못하는 중

from collections import deque

N,M = map(int,input().split())
graph = [list(input()) for _ in range(N)]

fvisited = [[0]*M for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]


jvisited = [[0]*M for _ in range(N)]

fq = deque()
jq = deque()

def fbfs():
    while fq:
        y,x = fq.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if fvisited[ny][nx] == 0 and graph[ny][nx] == '.':
                    fvisited[ny][nx] = fvisited[y][x]+1
                    fq.append((ny,nx))
    
    return (fvisited)

def jbfs(y,x):
    jvisited = [[0]*M for _ in range(N)]
    jvisited[y][x] = 0
    while jq:
        y,x = jq.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if jvisited[ny][nx] == 0 and graph[ny][nx] == '.':
                    if result[ny][nx]>=jvisited[y][x]+1: # 불 이동경로랑 비교했을 때
                        jvisited[ny][nx] = jvisited[y][x]+1
                        jq.append((ny,nx))
                    # else:
                    #     print("IMPOSSIBLE")
                    #     exit(0)

    return jvisited
    

for col in range(N):
    for row in range(M):
        if graph[col][row] == 'F':
            fq.append((col,row))
            fvisited[col][row] = 0

result = fbfs() # 2가지 이상일때는 이렇게 해야함

for col in range(N):
    for row in range(M):
        if graph[col][row] == 'J':
            jq.append((col,row))
            result2 = jbfs(col,row)

real_result = max(max(result)) #불
real_result2 = max(max(result2)) # 지훈

for col in range(N):
    print(result[col]) # 불

print()

for col in range(N):
    print(result2[col]) # 지훈이

print()
if real_result>real_result2:
    print(real_result2+1)

else:
    print("IMPOSSIBLE")


# if result2[0][M-1] == real_result2 or result2[N-1][M-1] == real_result2 or result2[0][0] == real_result2 or result2[N-1][0] == real_result2:
#     if real_result>real_result2:
#         print(real_result2+1)
    
#     else:
#         print("IMPOSSIBLE")

# else:
#     if real_result>real_result2:
#         print("IMPOSSIBLE")
