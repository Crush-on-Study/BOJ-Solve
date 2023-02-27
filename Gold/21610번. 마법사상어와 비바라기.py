import sys
sys.stdin = open('result.txt')

N,M = map(int,input().split())
# N은 격자 사이즈 , M은 명령 개수

graph,arr = [],[]


cloud = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]] # 1,1부터 시작하니까 0,0으로 해주기 위함

#     ←,↖, ↑,  ↗,→, ↘, ↓, ↙
dx = [-1,-1, 0, 1,1,1,0,-1] # 여기는 [y][x] 꼴이더라
dy = [0, -1,-1,-1,0,1,1, 1]


for _ in range(N):
    graph.append(list(map(int,input().split()))) # 그래프 싹다 만들어버림

for i in range(M):
    cmd = list(map(int,input().split())) # cmd[0]은 이동방향 , cmd[1]은 몇칸 이동?
    arr.append((cmd[0]-1,cmd[1]))

# print(graph)
# print(arr)

# 구름 이동 시작 1번
for i in range(M):
    next_cloud = []
    move = arr[i] # 첫번쨰 명령은
    d,s = move[0],move[1]
    for next in cloud:
        y,x = next[0],next[1] # 구름의 좌표
        #d,s = move[0],move[1]
        ny = (y + dy[d]*s)%N
        nx = (x + dx[d]*s)%N
        next_cloud.append([ny,nx])
    
    # print(cloud)
    # print(next_cloud)
    # break

# 각 구름에서 비가 내려서 해당 영역 물의 양 1씩 증가  2번
    visited = [[False]*N for _ in range(N)] # 5번 행동을 위한 밑밥
    for idx in next_cloud:
        y,x = idx[0],idx[1]
        graph[y][x]+=1
        visited[y][x] = True
    
    # print(cloud)
    # print(next_cloud)
    # print(graph)
    # print(visited)
    # break
    
    
# 구름 사라졋! 3번
    
    cloud = []

# 물복사버그 시작 4번
#    ↖,  ↗,  ↘,  ↙
    ay = [-1,-1,1,1]
    ax = [-1,1,1,-1]    
    
    for next in next_cloud:
        cnt = 0
        y,x = next[0],next[1]
        for i in range(4):
            ny = y+ay[i]
            nx = x+ax[i]
            if 0<=ny<N and 0<=nx<N:
                if graph[ny][nx] !=0:
                    cnt+=1
        
        graph[y][x]+=cnt
    
    # for col in graph:
    #     print(col)
    # break
    
# 구름이 생기고, 물 양 줄이는 것 5번        
    
    for col in range(N):
        for row in range(N):
            if graph[col][row]>=2:
                if not visited[col][row]:
                    graph[col][row]-=2
                    cloud.append([col,row])
                    

result = 0
for col in graph:
    result+=sum(col)

print(result)
