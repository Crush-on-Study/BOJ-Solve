# 재귀 연습용. 제한이 n<11이라서 딱 재귀 범위만큼만 가능함
# 원래 이런건 dp로 풀어야함

T = int(input())
for test_case in range(T):
    N = int(input())
    dp = [0,1,2,4] # 초기값 세팅

    def fibo(cnt):
        if N==cnt:
            dp.append(dp[cnt-1]+dp[cnt-2]+dp[cnt-3]) # 점화식
            return dp[-1]
        if N==1:
            return 1
        if N==2:
            return 2
        if N==3: # 1,1,1 / 1,2 / 2,1 / 3
            return 4
        else:
            dp.append(dp[cnt-1]+dp[cnt-2]+dp[cnt-3])
            return fibo(cnt+1)
        
    print(fibo(4))
