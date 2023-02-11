# 분명 어딘가 잘못된 부분이 있는데 찾질 못하겠다. 빙고 3개가 다 완성되지도 않았는데 중간에서 끊겨버리고 끝났다 왤까..?

graph = [list(map(int,input().split())) for _ in range(5)] # 빙고판 정보
delete_graph = [list(map(int,input().split())) for _ in range(5)] # 지울 순서

flag,bingo,cnt = 0,0,0
cross_check,cross_check2 = 100,100

def search(a):
    global flag,bingo,cnt
    global cross_check,cross_check2
    
    for col in range(5): # 얘는 기존 빙고판을 탐색해가면서
        for row in range(5):
            if graph[col][row] == a: # 전달받은 지울 값과 일치하는 값이 나오면
                graph[col][row] = -1 # 그걸 -1로 만들어버려
    
    for idx in range(5):
        cross_check+=graph[idx][idx]
    if cross_check == -5:
        bingo+=1
        
    for idx in range(5):
        cross_check2+=graph[idx][4-idx]
    if cross_check2 == -5:
        bingo+=1

    for col in range(5):  # 가로 체크
        if sum(graph[col]) == -5:
            bingo+=1
            
    new_graph = list(zip(*graph))
            
    for col in range(5):
        if sum(new_graph[col]) == -5:
            bingo+=1       
        
            
    return bingo


for col in range(5):  # 지울 순서의 행들에서
    for row in range(5): # 각각의 원소들을 탐색해
        cnt+=1
        a = delete_graph[col][row]
        result = search(a) # search함수에 전달해주고
        if result>=3:
            result = cnt
            break
    if result!=0:break
    
print(result)
