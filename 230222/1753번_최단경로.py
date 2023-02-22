import sys
input = sys.stdin.readline
import heapq

V,E = map(int,input().rstrip().split()) # 정점 / 간선
start = int(input().rstrip()) # 시작할 노드
graph = [[] for _ in range(V+1)]
inf = int(1e9)

weight = [inf] * (V+1)

for _ in range(E):
    a,b,c = map(int,input().rstrip().split()) # a에서 b노드로 가는데 c만큼의 비용이 든다
    graph[a].append((b,c))  # a노드 기준으로 b노드로 가는데 c의 비용에 대한 정보 받기


def stra(start):
    q = []
    heapq.heappush(q,(0,start)) # 배열과 (비용,시작노드)
    weight[start] = 0

    while q: # q에 (0,1) 들어가있고  비용 0 노드 1번이라는 뜻
        cost,now = heapq.heappop(q) # 가장 비용 짧은 애부터 pop시킴  갓 우선순위큐!
        if weight[now] < cost: # 현재 꺼내진 노드의 비용이 cost보다 작으면? 넘어가
            continue

        for idx in graph[now]:
            new_cost = cost+idx[1] # 비용 갱신
            if new_cost <weight[idx[0]]:
                weight[idx[0]] = new_cost
                heapq.heappush(q,(new_cost,idx[0]))

stra(start)

for i in range(1,V+1):
    if weight[i] == inf:
        print("INF")
    else:
        print(weight[i])
