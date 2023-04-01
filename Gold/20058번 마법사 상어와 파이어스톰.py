# N은 격자 사이즈, Q는 레벨 횟수
import copy
from collections import deque
N,Q = map(int,input().split())

_N = 2**N # 제곱 수라했으니까.

ice = []
for col in range(_N):
    ice.append(list(map(int,input().split())))

level = list(map(int,input().split()))

dx,dy = [1,0,-1,0],[0,1,0,-1]

### 위에 입력 이상 없음 ###
for idx in level:
    k = 2**idx # 레벨 단위로 해야하니까
    for col in range(0,_N,k):
        for row in range(0,_N,k):
            temp = []
            for small_col in range(col,col+k):
                temp.append(ice[small_col][row:row+k])

            for small_col in range(k):
                for small_row in range(k):
                    # 시계방향 회전
                    ice[col+small_row][row+k-small_col-1] = temp[small_col][small_row]

    
    ice_check = [[0]*_N for _ in range(_N)]
    for col in range(_N):
        for row in range(_N):
            cnt = 0
            for i in range(4):
                ny = col+dy[i]
                nx = row+dx[i]
                if 0<=ny<_N and 0<=nx<_N and ice[ny][nx]>0:
                    cnt +=1

            ice_check[col][row] = cnt

    for col in range(_N):
        for row in range(_N):
            if ice_check[col][row] < 3: # 인접 얼음이 3개 미만이면
                if ice[col][row] > 0: # 그리고 그 중심에 얼음이 있다면
                    ice[col][row] -= 1


### 위에꺼 다 끝내고 나면!
def bfs(y,x):
    global ccnt
    q = deque()
    q.append((y,x))

    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<_N and 0<=nx<_N:
                if not visited[ny][nx] and ice[ny][nx] > 0:
                    visited[ny][nx] = True
                    ccnt+=1
                    q.append((ny,nx))

    return ccnt


arr = []
visited = [[False]*_N for _ in range(_N)]
ccnt = 0
for col in range(_N):
    for row in range(_N):
        if ice[col][row] > 0 and not visited[col][row]:
            visited[col][row] = True
            ccnt = 1
            result = bfs(col,row)
            arr.append(result)

tot = 0
for col in range(_N):
    for row in range(_N):
        tot += ice[col][row]

if tot!=0:
    print(tot)
    print(max(arr))
    
else:
    print(tot)
    print(0)
