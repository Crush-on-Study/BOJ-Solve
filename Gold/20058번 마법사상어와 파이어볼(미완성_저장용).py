# 1,1 부터 시작함.
# N은 격자 사이즈, M은 파이어볼 개수 , K는 명령 개수
# m은 질량 / d는 방향 / s는 속력
# 세로,가로,질량,속력,방향

# 북,북동,동,남동,남,남서,서,북서
# 0,1,2,3,4,5,6,7
dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]

N,M,K = map(int,input().split()) # 격자 사이즈, 파이어볼 개수, 명령 개수

coor,info = [],[] # coor 위치 담을 리스트 info는 질량/속력/방향

graph = [[0]*N for _ in range(N)] # 그래프 초기화. 모두 0에서 시작, 단 파이어볼 있는 곳 제외
for i in range(M):
    cmd = list(map(int,input().split())) # 세로/가로 , 질량, 속력 , 방향
    y,x = cmd[0],cmd[1]
    m,s,d = cmd[2],cmd[3],cmd[4]
    coor.append((y,x))
    info.append((m,s,d))
    graph[y-1][x-1] = m  # 1,1에서 시작하니까!

velocity = []
# 1번 파이어볼 이동 시작
for j in range(M):
    
    fire = 1
    y,x = coor[j][0],coor[j][1] # 
    m,s,d = info[j][0],info[j][1],info[j][2]
    
    ny = (y+dy[d]*s)%N
    nx = (x+dx[d]*s)%N # 1번이랑 N번이랑 연결되어있다 하니까!

# 2-1 2개 이상의 파이어볼이 있는 칸 합치기
    if graph[ny-1][nx-1] == 0:
        graph[ny-1][nx-1] = m
        velocity.append(info[j][1])
    else:
        graph[ny-1][nx-1]+=graph[y-1][x-1]
        velocity.append(info[j][1])
        fire+=1
    graph[y-1][x-1] = 0 # 옮겨갔으니 초기화

# 2-2 합쳐진 파이어볼 질량을 나누기 / 속력 구하기
y,x = ny,nx
graph[y-1][x-1] = graph[y-1][x-1]//5 # 합쳐진 파볼 질량을 5로 나눔
velo = sum(velocity)
s = velo//fire

# 2-3 파이어볼 방향이 홀수/짝수?
for idx in info:
    if idx[2]%2==0:
        pass
