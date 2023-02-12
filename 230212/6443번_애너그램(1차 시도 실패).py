# 단순 백트래킹 문제인줄 알았으나 시간초과가 난 풀이
# 줄일 수 있는 방법 찾아봐야겠다 (pypy로 제출 시, 메모리 초과임)

import sys
input = sys.stdin.readline

T = int(input().rstrip())

for test_case in range(T):
    s = input().rstrip() # 문자열 입력받고
    arr = [idx for idx in s]
    visited = [False]*(len(arr)+1)
    arr2 = []
    result_box = []

    def backtrack(num):
        if num==len(arr):
            result_box.append(''.join(map(str,arr2)))
            return
        
        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                arr2.append(arr[i])
                backtrack(num+1)
                visited[i] = False
                arr2.pop()
                
        return result_box
                
    result = list(set(backtrack(0)))
    result.sort()

    for idx in result:
        print(idx)
