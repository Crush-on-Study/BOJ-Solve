# 첫 풀이 (실패)
# 첫 풀이 때, 실패한 부분을 현재 풀이와 비교하기 위해 저장

import sys

N = int(input()) # 격자 사이즈
dx,dy = [1,0,-1,0],[0,1,0,-1]
graph = [[0]*(N) for _ in range(N)] # (1,1)부터 시작함

arr = []
for i in range(N**2):
    arr.append(list(map(int,input().split())))


love = []
for idx in arr:
    num,a,b,c,d = idx # 학생의 번호와 좋아하는 학생들의 번호 -> 이럴 땐 그냥 리스트 슬라이싱으로 접근하자

    # 1번 행동 모두 빈칸인 경우 
    zero_check = 0
    for col in range(N):
        for row in range(N):
            if graph[col][row] != 0:
                zero_check+=1
                love.append((graph[col][row],col,row)) # 그 사람 번호, 좌표

    # 전부 빈칸이라면 쉽게쉽게 가자. 정중앙에 박고 시작함
    if zero_check==0:
        y,x = N//2,N//2
        graph[y][x] = num
    
    # 2번 행동 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸
    else: # 전부 빈칸이 아닌 경우라면? love배열에 누군가 들어있겠다.
        for lovee in love: # 누군가를 꺼냈는데
            if lovee in [a,b,c,d]: # 좋아하는 사람 중 한명이라면
                check = []
                for i in range(4):
                    ny = lovee[1]+dy[i]
                    nx = lovee[2]+dx[i] # 방향 탐색해서
                    if 0<=ny<N and 0<=nx<N:
                        check.append((ny,nx)) # 범위 안벗어나는 선에서 좌표 담고
                        check.sort() # 좌표 정렬해서


for col in graph:
    print(col)
