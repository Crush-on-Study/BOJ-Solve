graph = [list(map(int,input().split())) for _ in range(5)] # 빙고판 정보
delete_graph = [list(map(int,input().split())) for _ in range(5)] # 지울 순서

def search(a):
    for col in range(5):
        for row in range(5):
            if graph[col][row] == a:
                graph[col][row] = 0
                
    return graph

def bingo_check():
    bingo = 0
    check,check2 = 0,0
    for col in range(5):
        if sum(graph[col]) == 0 : bingo+=1
        
    for col in range(5):
        temp = 0
        for row in range(5):
            temp+=graph[row][col]
        if temp==0 : bingo+=1
            
    for idx in range(5):
        check+=graph[idx][idx]
    if check==0 : bingo+=1
    
    for idx in range(5):
        check2+=graph[idx][4-idx]
    if check2==0 : bingo+=1
    
    return bingo

cnt = 0
real_result = 0
for col in range(5):
    for row in range(5):
        a = delete_graph[col][row]
        cnt+=1
        result = search(a)
        if bingo_check()>=3:
            real_result = cnt
            break
    if real_result!=0 : break
        
print(real_result)
