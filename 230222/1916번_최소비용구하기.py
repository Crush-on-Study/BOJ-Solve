import heapq

N = int(input()) # 노드 개수
M = int(input()) # 간선 개수

inf = int(1e9)

graph = [[] for _ in range(N+1)]
money = [inf]*(N+1)

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

start,end = map(int,input().split())

def stra(start):
    q = []
    heapq.heappush(q,(0,start)) # 처음엔 비용 0, 시작 노드
    money[start] = 0

    while q:
        cost,now = heapq.heappop(q) # 비용, 현재 위치
        if money[now] < cost: # 지금의 비용이 < 힙에서 꺼낸 비용보다 작으면
            continue # 갱신할 필요없지
        
        for i in graph[now]: # 힙에서 꺼낸 노드의 주변을 탐색하는데
            new_cost = cost+i[1] # 목적지 노드로 가는데 드는 비용 + 기존 비용 
            if new_cost< money[i[0]]: 
                money[i[0]] = new_cost
                heapq.heappush(q,(new_cost,i[0]))

stra(start)
print(money[end])
