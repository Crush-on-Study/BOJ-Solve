# 직사각형 발상이 어려웠던 문제

import sys
input = sys.stdin.readline

N,I,M = map(int,input().rstrip().split())
info = []
for _ in range(M):
    sx,sy = map(int,input().rstrip().split())
    info.append((sx-1,sy-1))

answer = 0

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def move(sx,sy,l1,l2):
    global answer
    save_l1 = l1
    save_l2 = l2
    d = 0 # 방향

    while d!=4:
        if d in [0,2]: # x방향 이동
            save_l1 -= 1
            sx = sx+dx[d]
            if not save_l1:
                d+=1
                save_l1 = l1 # 채워주고

        elif d in [1,3]: # y방향 이동
            save_l2 -= 1
            sy = sy+dy[d]
            if not save_l2:
                d+=1
                save_l2 = l2 # 채워주고

        if sx>=0 and sy>=0: # 범위 안에 들어가 있으면
            ex = sx+l1
            ey = sy+l2
            answer = max(answer,fish(sx,sy,ex,ey))

def fish(sx,sy,ex,ey):
    cnt = 0
    for x,y in info:
        if sx<=x<=ex and sy<=y<=ey: # 그물 범위 안에 물고기 있으면
            cnt+=1

    return cnt


for sx,sy in info:
    for l1 in range(1,I//2):
        l2 = I//2-l1 # (1,4)
        move(sx-l1,sy-l2,l1,l2)

print(answer)
