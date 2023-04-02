# 격자 사이즈, 박멸 진행 횟수, 제초제 확산 범위, 제초제가 남아있는 년 수
N,M,K,C = map(int,input().split())
ori_K,ori_C = K,C
# 빈칸은 0, 벽은 -1
graph = []
for col in range(N):
    graph.append(list(map(int,input().split())))

ori_graph = [a[:] for a in graph]

# 제초제 뿌려진 곳 확인
toxic = [[0]*N for _ in range(N)]

# 번식
dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 제초제
tox = [1,1,-1,-1]
toy = [1,-1,1,-1]

# 0번 행동 : 제초제 시간 지날 때
def zero():
    for col in range(N):
        for row in range(N):
            if toxic[col][row] > 0:
                toxic[col][row] -= 1

# 1번 행동 : 나무 성장  문제 없음
def first():
    for col in range(N):
        for row in range(N):
            if graph[col][row] > 0:
                cnt = 0
                for i in range(4):
                    ny = col+dy[i]
                    nx = row+dx[i]
                    if 0<=ny<N and 0<=nx<N:
                        if graph[ny][nx] > 0: # 벽이 아니고 나무가 있는 경우
                            cnt+=1
                    
                graph[col][row] += cnt

# 2번 행동 : 나무 번식  문제 없음 
def second():
    temp = [[0]*N for _ in range(N)]
    for col in range(N):
        for row in range(N):
            if graph[col][row] > 0:
                ccnt = 0
                for i in range(4):
                    ny = col+dy[i]
                    nx = row+dx[i]
                    if 0<=ny<N and 0<=nx<N:
                        if graph[ny][nx] == 0 and not toxic[col][row]: # 아무것도 없을 때
                            ccnt+=1
                
                for i in range(4):
                    ny = col+dy[i]
                    nx = row+dx[i]
                    if 0<=ny<N and 0<=nx<N:
                        if graph[ny][nx] == 0:
                            temp[ny][nx] += graph[col][row]//ccnt
    
    for col in range(N):
        for row in range(N):
            if temp[col][row]>0:
                graph[col][row] = temp[col][row]
    
    for col in range(N):
        for row in range(N):
            ori_graph[col][row] = graph[col][row]


# 3번 행동 : 제초제 뿌릴 곳 탐색 문제 없음
def third():
    global K
    temp = [a[:] for a in graph]
    for col in range(N):
        for row in range(N):
            if graph[col][row] > 0: # 나무가 있는 곳에
                ans = 0
                cnt = 1
                check = -111
                while cnt<=K:
                    for i in range(4):
                        if i == check:
                            break
                        ny = col+toy[i]*cnt
                        nx = row+tox[i]*cnt
                        if 0<=ny<N and 0<=nx<N:
                            if graph[ny][nx] > 0:
                                ans += graph[ny][nx]
                            elif graph[ny][nx] == -1:
                                check = i
                    cnt+=1

                temp[col][row] += ans
                K = ori_K

    for col in range(N):
        for row in range(N):
            graph[col][row] = temp[col][row]


# 4번 행동 : 최대값 찾기 문제 없음
def forth():
    max_check = -100
    place = [] # 박멸시킬 최대 나무가 동일한 경우

    for col in range(N):
        for row in range(N):
            max_check = max(max_check,graph[col][row])

    for col in range(N):
        for row in range(N):
            if graph[col][row] == max_check:
                place.append((graph[col][row],col,row))
    
    return place[0]

# 5번 행동 : 제초제 전파
def five(result):
    value,col,row = result
    arr.append(value)
    graph[col][row] = -100
    toxic[col][row] = C
    cnt = 1
    while cnt<5:
        for i in range(4):
            ny = col+toy[i]*cnt
            nx = row+tox[i]*cnt
            if 0<=ny<N and 0<=nx<N:
                if graph[ny][nx] > 0:
                    graph[ny][nx] = -100 # 제초제 뿌려진 곳임
                    toxic[ny][nx] = C # 표식 남음

        cnt+=1

    for col in range(N):
        for row in range(N):
            if graph[col][row] == -100:
                ori_graph[col][row] = graph[col][row]

    for col in range(N):
        for row in range(N):
            graph[col][row] = ori_graph[col][row]
    
    return arr

arr = []
for _ in range(M):
    zero()
    first()
    second()
    third()
    result = forth()
    arr = five(result)

print(sum(arr))
