N,M = map(int,input().split())
nums = sorted(list(map(int, input().split())))
visited = [False]*(N+1)
arr = []

def backtrack():
    if len(arr) == M:
        print(*arr)
        return
        
    check = 0
    for i in range(N):
        if not visited[i] and check != nums[i]:
            visited[i] = True
            arr.append(nums[i])
            check = nums[i]
            backtrack()
            visited[i] = False
            arr.pop()

backtrack()

# set을 쓰지않고도 중복제거를 할 수 있다. set을 쓰면 시간초과가 난다
# 이걸로 애너그램도 다시 
