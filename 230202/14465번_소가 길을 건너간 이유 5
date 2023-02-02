import sys
input = sys.stdin.readline
N,K,B = map(int,input().split())
arr = [0]*(N+1)
for i in range(B):
    arr[int(input())] = 1
cmp =[]
cnt = 0
for i in range(N+1):
    cnt+=arr[i]
    cmp.append(cnt)

for i in range(N+1-K):
    B = min(B,cmp[i+K]-cmp[i])
print(B)
