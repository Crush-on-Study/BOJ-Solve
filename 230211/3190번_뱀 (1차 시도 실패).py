import sys
sys.stdin = open("111.txt")

N = int(input()) # 격자판 사이즈
graph = [[0]*N for _ in range(N)] # 격자 정보받기
length = 1 # 뱀 길이

apple = int(input()) # 사과 개수
apple_lst = []

for cnt in range(apple):
    y,x = map(int,input().split()) # 사과 좌표
    apple_lst.append((y-1,x-1)) # 인덱스 0번째 시작인거 고려해서
    
snake_move = int(input()) # 뱀의 이동 방향 및 시간
snake_lst = [] # 뱀 이동 리스트에 담을 것

for cnt in range(snake_move):
    sec,direction = input().split()
    snake_lst.append((sec,direction))
    
dx = [1,0,-1,0]
dy = [0,-1,0,1] # 동 북 서 남

time,flag = 0,0

def apple_search(y,x):
    global length
    for idx in range(len(apple_lst)):
        if apple_lst[idx][0]==y and apple_lst[idx][1]==x: # 사과가 있는 곳에 도착했다면
            length+=1 # 뱀 길이 늘려
        else:
            return        
    return length

    
def search(y,x): # 뱀의 처음 위치 0,0 전달받고
    global time,flag
    while True:
        if flag == 1:
            break
        nx = x+dx[0] # 계속 동쪽으로 움직이다가요
        ny = y+dy[0]
        y = ny
        x = nx
        time+=1 # 움직일때마다 카운트 카운트
        # apple_search(ny,nx)
        
        for idx in range(len(snake_lst)):
            if time==int(snake_lst[idx][0]):
                if snake_lst[idx][1] == 'L': # 왼쪽 = L
                    nx = x+dx[1]
                    ny = y+dy[1] # 바로 북쪽으로 틀어
                    if 0>nx or nx>=N or 0>ny or ny>=N: # 근데 그게 벽이야 그럼 나가
                        flag = 1
                        break
                    else:
                        y = ny
                        x = nx # 좌표 갱신
                        apple_search(y,x)     
        
    return time

search(0,0)


# 함수를 구조화할 필요가 있음. 각 기능을 나눠서 생각해보자 천천히. 천천히 가자
