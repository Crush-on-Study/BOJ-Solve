import sys
input = sys.stdin.readline
# N 격자 , M 진행 연수, K 제초제 확산 범위, C 남아있는 년수

N,M,K,C = map(int,input().rstrip().split())

graph = []
for col in range(N):
    graph.append(list(map(int,input().rstrip().split())))
    
dx,dy = [1,0,-1,0],[0,1,0,-1]

cx = [1,1,-1,-1]
cy = [-1,1,-1,1] # 제초제

toxic = [[0]*N for _ in range(N)] # 제초제

tot_kill = 0 # 정답
    
# 1번 나무 성장
def first():
    for col in range(N):
        for row in range(N):
            if graph[col][row]>0:
                cnt = 0
                for i in range(4):
                    ny = col+dy[i]
                    nx = row+dx[i]
                    if 0<=ny<N and 0<=nx<N and graph[ny][nx]>0:
                        cnt+=1        
                graph[col][row] += cnt

# 2번 나무 번식
def second():
    temp = [[0]*N for _ in range(N)]
    for col in range(N):
        for row in range(N):
            if graph[col][row] > 0:
                cnt = 0
                for i in range(4):
                    ny = col+dy[i]
                    nx = row+dx[i]
                    # 1. 격자 안벗어나고 / 벽 아니고, 다른 나무 없고 / 제초제없음
                    if 0<=ny<N and 0<=nx<N and not graph[ny][nx] and not toxic[ny][nx]:
                        cnt += 1
                        
                for i in range(4):
                    ny = col+dy[i]
                    nx = row+dx[i]
                    if 0<=ny<N and 0<=nx<N and not graph[ny][nx] and not toxic[ny][nx]:
                        temp[ny][nx] += graph[col][row] // cnt
                        
    for col in range(N):
        for row in range(N):
            graph[col][row] += temp[col][row]
                

# 4번. 제초제 유지여부
def forth():
    for col in range(N):
        for row in range(N):
            if toxic[col][row] > 0:
                toxic[col][row] -= 1
           
# 3번 제초제 뿌리기 전에 최대 박멸할 수 있는 곳 찾기
def third():
    temp = [[0]*N for _ in range(N)]
    for col in range(N):
        for row in range(N):
            if graph[col][row] > 0: # 나무가 있는 경우
                kill_tot = 0
                side = [] # 더 이상 진행하지 말아야할 방향을 담는 것
                for k in range(1,K+1):
                    for i in range(4):
                        ny = col+cy[i]*k
                        nx = row+cx[i]*k
                        # 격자를 안벗어나고, 진행해도 되는 방향인 경우에만
                        if 0<=ny<N and 0<=nx<N:
                            if i in side:
                                continue
                            
                            else:
                                if graph[ny][nx] == -1:  # 벽 만났으면 그때의 방향 담고
                                    side.append(i)
                                    continue
                                
                                if graph[ny][nx] == 0: # 빈칸 만났으면 그때의 방향 담고
                                    side.append(i)
                                    continue
                                
                                # 문제 없으면 연산
                                kill_tot += graph[ny][nx]
                                
                temp[col][row] += kill_tot  # 해당 좌표에서 죽일 수 있는 나무 그루 수
                                          
            ### 5:07 시작 -> 5:35 저녁 // 7:29분 재시작 -> 8:58분 GG
                
    for col in range(N): 
        for row in range(N):
            if graph[col][row] != -1: # 벽이 아닌 곳
                temp[col][row] += graph[col][row] # graph꺼 받아와서 연산
    
    max_kill = 0
    for col in range(N):
        for row in range(N):
            max_kill = max(max_kill,temp[col][row]) # 최대값 찾기
    
    arr = []
    flag = 0
    for col in range(N):
        if flag:break
        for row in range(N):
            if temp[col][row] == max_kill: # 최대값 좌표 찾아서
                arr.append((max_kill,col,row)) # arr에 담고 끝내기. 같은 최대값이면 행,열이 작을수록이므로.
                flag = 1
                break
                
    return arr



# 5번. 나무 박멸 -> 제초제 뿌리기
def fifth(arr):
    global tot_kill
    max_kill,max_y,max_x = arr[0]
    if max_kill > 0:
        toxic[max_y][max_x] = C
        graph[max_y][max_x] = 0
        side = []
        for k in range(1,K+1):
            for i in range(4):
                ny = max_y+cy[i]*k
                nx = max_x+cx[i]*k
                # 격자를 안벗어나고, 진행해도 되는 방향인 경우에만
                if 0<=ny<N and 0<=nx<N:
                    if i in side:
                        continue
                    else:
                        if graph[ny][nx] == -1:
                            side.append(i)
                            toxic[ny][nx] = C
                            continue
                        
                        if graph[ny][nx] == 0:
                            side.append(i)
                            toxic[ny][nx] = C
                            continue
                        
                        toxic[ny][nx] = C
                        graph[ny][nx] = 0
    
    tot_kill += max_kill
       
for _ in range(M):
    first()      
    second()
    forth()
    result = third()
    fifth(result)
    
print(tot_kill)                    
