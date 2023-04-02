import sys
import copy

input = sys.stdin.readline

graph = []
for idx in range(4):
    graph.append(list(map(int,input().rstrip().split())))

new_graph = [[0]*4 for _ in range(4)]
for idx in range(4):
    new_graph[idx][0] = [graph[idx][0],graph[idx][1]-1]
    new_graph[idx][1] = [graph[idx][2],graph[idx][3]-1]
    new_graph[idx][2] = [graph[idx][4],graph[idx][5]-1]
    new_graph[idx][3] = [graph[idx][6],graph[idx][7]-1]
    
#        ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 
dic = {0:(-1,0),1:(-1,-1),2:(0,-1),3:(1,-1),4:(1,0),5:(1,1),6:(0,1),7:(-1,1)}
max_check = 0

def move(sy,sx,eat,new_graph):
    global max_check
    eat+=new_graph[sy][sx][0]
    new_graph[sy][sx][0] = 0 # 상어가 있어요.

    for idx in range(1,17): # 1번 물고기부터 17번 물고기까지
        flag = False
        for col in range(4):
            for row in range(4):
                if new_graph[col][row][0] == idx:
                    flag = (col,row)
                    
        if not flag:
            continue
        
        col,row = flag
        x = new_graph[col][row][1]        
        for i in range(8):
            d = (x+i)%8 # 8방향 반시계 45도 회전함
            ny = col+dic[d][0]
            nx = row+dic[d][1]
            if 0<=ny<4 and 0<=nx<4:
                if (ny,nx) != (sy,sx):
                    new_graph[col][row][1] = d
                    new_graph[col][row],new_graph[ny][nx] = new_graph[ny][nx],new_graph[col][row]
                    break
    
    max_check = max(max_check,eat)
    ############# 위에 물고기 이동 완료
    shark_d = new_graph[sy][sx][1] # 상어의 이동방향
    for i in range(1,4):
        ny = sy + (dic[shark_d][0]*i)
        nx = sx + (dic[shark_d][1]*i)
        if 0<=ny<4 and 0<=nx<4 and new_graph[ny][nx][0]>0:
            move(ny,nx,eat,copy.deepcopy(new_graph))      

move(0,0,0,new_graph)
print(max_check)
