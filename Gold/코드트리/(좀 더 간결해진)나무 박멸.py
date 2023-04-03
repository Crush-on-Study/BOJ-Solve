import sys
input = sys.stdin.readline

# 격자 사이즈 / 박멸이 진행되는 해 / 제초제 확산 범위 / 제초제가 남아있는 년 수
N,M,K,C = map(int,input().rstrip().split())

# 그래프 정보
graph = []
for col in range(N):
    graph.append(list(map(int,input().rstrip().split())))

dx,dy = [1,0,-1,0],[0,1,0,-1]
tox = [1,-1,-1,1]
toy = [1,1,-1,-1]

toxic = [[0]*N for _ in range(N)] # 제초제 그래프

result = [] # 결과값 담을 배열

# 1번 행동 나무 성장 (완료)
def first():
    for col in range(N):
        for row in range(N):
            if graph[col][row] > 0:
                cnt = 0

                for i in range(4):
                    ny = col+dy[i]
                    nx = row+dx[i]
                    if 0<=ny<N and 0<=nx<N and graph[ny][nx] > 0:
                        cnt+=1

                graph[col][row] += cnt


# 2번 행동 나무 번식 (완료)
def second():
    temp = [[0]*N for _ in range(N)]
    for col in range(N):
        for row in range(N):
            if graph[col][row] > 0:
                cnt = 0
                for yy,xx in zip(dy,dx):
                    ny = col+yy
                    nx = row+xx
                    # 1. 격자 안벗어나고 , 2. 제초제 없고 , 3. 벽 없고, 다른 나무 없는 경우
                    if 0<=ny<N and 0<=nx<N and not toxic[ny][nx] and not graph[ny][nx]:
                        cnt+=1
                    
                
                for yy,xx in zip(dy,dx):
                    ny = col+yy
                    nx = row+xx
                    if 0<=ny<N and 0<=nx<N and not toxic[ny][nx] and not graph[ny][nx]:
                        temp[ny][nx] += graph[col][row] // cnt 
                    

    for col in range(N):
        for row in range(N):
            graph[col][row] += temp[col][row]


# 4번 행동 제초제 사라지기
def forth():
    for col in range(N):
        for row in range(N):
            if toxic[col][row] > 0:
                toxic[col][row] -= 1


# 3번 행동 나무 최대박멸 찾기 (완료.. 근데 이상한데..?)
def third():
    temp = [[0]*N for _ in range(N)]
    mmax_check,max_y,max_x = 0,0,0
    for col in range(N):
        for row in range(N):
            if graph[col][row] > 0:
                cnt = graph[col][row]
                for yy,xx in zip(toy,tox):
                    y,x = col,row
                    for _ in range(K):
                        y,x = y+yy , x+xx # 이거 좋은 스킬이네
                        if (0<=y<N and 0<=x<N) and graph[y][x] > 0:
                            cnt+=graph[y][x]
                        else:
                            break

                if mmax_check < cnt:
                    mmax_check = cnt
                    max_y = col
                    max_x = row

    result.append(mmax_check)

    if graph[max_y][max_x] > 0:
        graph[max_y][max_x] = 0
        toxic[max_y][max_x] = C

        for yy,xx in zip(toy,tox):
            y,x = max_y,max_x
            for _ in range(K):
                y = y+yy
                x = x+xx
                if not (0<=y<N and 0<=x<N):
                    break

                if graph[y][x] < 0:
                    break

                if graph[y][x] == 0:
                    toxic[y][x] = C
                    break
                
                graph[y][x] = 0
                toxic[y][x] = C

for _ in range(M):
    first()
    second()
    forth()
    third()
    
print(sum(result))
