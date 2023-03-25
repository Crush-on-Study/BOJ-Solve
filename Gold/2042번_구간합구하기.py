# 0번. 세그먼트 트리를 배열의 각 구간 합으로 채우기
def init(start,end,index): # start = 배열 시작 인덱스 , end = 배열의 마지막 인덱스 ,
    # index = 세그먼트 트리 인덱스
    if start == end: # 가장 끝 노드에 도달한 경우 arr을 tree에 삽입
        tree[index] = arr[start]
        return tree[index]
    
    mid = (start+end)//2
    tree[index] = init(start,mid,index*2) + init(mid+1,end,index*2+1)
    return tree[index]

# 세그먼트 트리 최상단 노드를 기준으로,
# 왼쪽은 *2 , 오른쪽은 *2 + 1로 체크. (이진트리를 기반으로 함)

# 1번. 구간 합 구하는 함수
# left,right : 구간 합을 구하고자 하는 범위
def interval_sum(start,end,index,left,right):
    # 범위 밖에 있는 경우
    if left > end or right < start:
        return 0
    
    if left <= start and right >= end:
        return tree[index]
    
    mid = (start+end)//2
    return interval_sum(start,mid,index*2,left,right) + interval_sum(mid+1,end,index*2+1,left,right)

# 2번. 업데이트 : 노드 데이터가 바뀐 경우, 관련 노드들 재귀로 갱신
# what : 수정하고자 하는 노드
# value : 수정할 값
def update(start,end,index,what,value):
    if what < start or what > end:
        return
    
    tree[index] += value
    if start == end:
        return
    
    mid = (start+end)//2
    update(start,mid,index*2,what,value)
    update(mid+1,end,index*2+1,what,value)
    
###################################################3
    
N,M,K = map(int,input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))
    
tree = [0]* (len(arr)*4) # 세그먼트 트리 구조
init(0,len(arr)-1,1) # arr 배열의 범위 , 세그먼트트리 인덱스 시작번호


for idx in range(M+K):
    a,b,c = map(int,input().split())
    
    if a==1: # b번째 수를 c로 바꾸기
        b-=1
        change = c-arr[b]
        arr[b] = c
        update(0,len(arr)-1,1,b,change)
        
    elif a==2: # b부터 c까지의 합 구하기
        print(interval_sum(0,len(arr)-1,1,b-1,c-1))
    
