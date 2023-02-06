D,K = map(int,input().split()) # D 날짜  K 떡
dp = [0 for i in range(D)]
dp[0],dp[1] = 1,1
while True:
    for i in range(2,D):
        dp[i] = dp[i-1]+dp[i-2]
        
    if dp[D-1] == K:
        print(dp[0],dp[1],sep="\n")
        break
    elif dp[-1]>K: # D까지 가지도 않았는데 초과한다면?
        dp[0]+=1 # 첫날 떡 개수 카운팅
        dp[1] = dp[0] # dp[1]에도 똑같이 복사
    else: # dp[-1]<K라면
        dp[1]+=1 # 두번째 계속 올림
        
# 첫 트라이 실패하고 구글링으로 힌트 얻은 문제. 초기값이 정해진 DP가 아니라서
# 처음엔 탑다운 형식으로 찾아가고자 했다.
# K,K//2 를 지금의 dp[0] , dp[1] 같은 형식으로 하고  dp[now] < dp[next] 인 경우 빠꾸하고  K//2 + 1씩 카운팅해줄 생각이었다
# 아이디어는 비슷했는데 아직 구현 실력이 너무 딸린다
# 언제쯤 힌트없이도 풀까? 너무 한심하다
