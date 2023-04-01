# N은 격자 사이즈, M은 바이러스 개수, K는 사이클 횟수
N,M,K = map(int,input().split())

# 초기 배양액
init_eat = [[5]*N for _ in range(N)]

# 사이클 1회 마치고 추가될 양분
add_eat = []
for col in range(N):
    add_eat.append(list(map(int,input().split())))

# 바이러스 정보들
virus = [[[] for _ in range(N)] for _ in range(N)]
for col in range(M):
    y,x,age = map(int,input().split())
    virus[y-1][x-1].append(age)

# 방향 키
step = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

#### 입력 이상 X ####

# 1번/2번 행동 시작
def eating():
    for col in range(N):
        for row in range(N):
            if virus[col][row]: # 바이러스가 있는 곳이라면
                virus[col][row].sort() # 나이가 어린 바이러스부터 먹어야하므로,
                temp = []
                dead = 0
                for age in virus[col][row]:
                    if age <= init_eat[col][row]: # 양분이 나이보다 크거나 같을 경우
                        init_eat[col][row] -= age
                        age+=1
                        temp.append(age)

                    else:
                        dead += age//2 # 현재 나이의 절반만큼의 양분

                init_eat[col][row] += dead
                virus[col][row].clear() # 한번 싹 치워주고
                virus[col][row].extend(temp)


# 3번 행동 시작
def grow():
    for col in range(N):
        for row in range(N):
            if virus[col][row]: # 바이러스가 있다면
                for age in virus[col][row]:
                    if age%5==0:
                        for idx in step:
                            ny = col+idx[0]
                            nx = row+idx[1]
                            if 0<=ny<N and 0<=nx<N:
                                virus[ny][nx].append(1) # 나이가 1인 나무 추가

for _ in range(K):
    eating()
    grow()
    for col in range(N):
        for row in range(N):
            init_eat[col][row] += add_eat[col][row]

tot = 0
for col in range(N):
    for row in range(N):
        if virus[col][row]:
            tot += len(virus[col][row])

print(tot)
