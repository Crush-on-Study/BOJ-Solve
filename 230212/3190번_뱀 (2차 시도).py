N = int(input()) # 격자판 사이즈
graph = [[0]*(N+1) for _ in range(N+1)] # 격자 정보받기 N+1을 한 이유는 0,0 시작이 아닌 1,1이라서 그래

apple = int(input()) # 사과 개수
for _ in range(apple):
    a,b = map(int,input().split())
    graph[a][b] = 1 # 사과 있는 곳을 1로 치환
    
snake_move = int(input()) # 뱀의 이동 방향 및 시간
snake_lst = [] # 뱀 이동 리스트에 담을 것

for cnt in range(snake_move):
    sec,direction = input().split()
    snake_lst.append((int(sec),direction))
    
dx = [1,0,-1,0]
dy = [0,1,0,-1] # 동 남 서 북


def rotate(d,direction): # 현재 바라보는 방향이랑 변환하려는 알파벳 전달받아
    if direction == 'L':
        d = (d-1)%4 # 왼쪽이면 고개 돌려
    else:
        d = (d+1)%4 # 오른쪽이면 고개 돌려
    return d


def search(): # 전달을 안받네? 왜지?
    y,x = 1,1 # 현재 뱀의 위치
    graph[y][x] = 2 # 뱀의 위치를 2로 치환
    d = 0 # 현재 바라보는쪽은 동쪽
    time = 0 # 걸리는 시간
    idx = 0
    q = [(x,y)]
    while True:
        ny = y+dy[d]
        nx = x+dx[d] # 이동해
        if 1<=ny<=N and 1<=nx<=N and graph[ny][nx]!=2: # 맵 범위 안에 있고 뱀 꼬리랑 마주하지 않는다면
            if graph[ny][nx] == 0: # 사과가 없는 곳이라면
                graph[ny][nx] = 2 # 뱀 머리를 위치시키고
                q.append((ny,nx)) # 뱀 위치 받아주고
                px,py = q.pop(0) # 꼬리 제거
                graph[px][py] = 0
                
            
            if graph[ny][nx] == 1: # 사과가 있다면
                graph[ny][nx] = 2 # 뱀 머리 위치시키고
                q.append((ny,nx))
        
        else:
            time+=1
            break
        
        y,x = ny,nx # 좌표갱신
        time+=1
        
        if idx<snake_move and time == snake_lst[idx][0]: # 움직일 시간이 되었다면
            d = rotate(d,snake_lst[idx][1])
            idx+=1
            
    return time

print(search())

# 풀이를 결국 참고해버린..
# 그래프를 여러개 세우지말고, 주어진 그래프 하나에서 각자 사물을 표시할 넘버링을 하는게 좋다 0,1,2 이런 식으로
# 그리고 함수로 구조화하는건 매우매우 중요하다. 거의 다 왔는데 왜 틀렸었을까
# 함수에 대한 공부가 더 
