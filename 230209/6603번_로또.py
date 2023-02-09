from collections import deque # 0. 데큐 쓰기 위함
def backtrack(start): # 8. 0 전달받았음. 여기서 0은 카운팅을 말함    # 15. 이제 1 전달 받음
    if len(num) == 6: # 9. 배열 num의 길이가 6이 되었다면? (즉, 로또 자릿수들이 완성되었다면)  # 16. num길이가 6이니?
        print(' '.join(map(str,num))) 
        if num[0] == arr[k-6]: #
            return
        return
    check = 0  
    for i in range(start, k): # 10. 만약 아직 num의 길이가 6이 아니라면? 루핑시작하는데, start는 0이니까 0부터 시작해서 로또 번호 개수만큼 받음
      # 17. 아직 아니네, 그럼 for문은 1,6까지 시작이니까
        if arr[i] not in num and check < arr[i]: # 11. arr[0]이 num에 없고, check< arr[0] 이라면?  # 18. arr[1] = 2고 check는 현재 1이고 arr[1]보다 작으니까
            num.append(arr[i]) # 12. num에 박아 # 19. num에 박아
            check = arr[i] # 13. 그리고 check는 이제 arr[0]가 된다.  이게 무슨 의미냐면 오름차순을 말하는거임 1 2 3 4 5 6 / 1 2 3 4 5 7.. 이런 식으로 ㅇㅇ
            # 20. check는 다시 arr[1]로 갱신되고
            backtrack(i+1) # 14. 재귀호출 시작 # 21. 재귀호출 시작...
            num.pop()
            
while True: # 1. 무한루핑 돌리면서
    arr = list(map(int, input().split()))  # 2. 번호 개수와 번호들 입력받음
    arr = deque(arr) # 3. 그 후 popleft쓰기 위해 데큐로 변환하고 
    k = arr.popleft() # 4. 제일 앞에놈 꺼내고 변수에 따로 저장해둬서
    if k == 0: # 5. 0이면 빠져나가도록 함
        break
    num = [] # 6. 결과값 담아놓을 리스트 (로또 6자리 숫자 담을 배열 ㅇㅇ)
    backtrack(0) # 7. 함수 호출 시작
    print()
