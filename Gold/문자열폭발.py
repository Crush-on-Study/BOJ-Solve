# 골드4 문자열폭발 / 굉장히 유용한 스킬인듯
# 아이디어가 좋다. 언젠간 다시 쓰일 법하다.
# 스택,
N,M = map(int,input().split())

S = input() # 얘 기준으로 필터링 할 것
P = input() # 문자열

bomb = [idx for idx in S]
lst = []

for idx in range(len(P)):
	lst.append(P[idx])
	if lst[-1] == bomb[-1] and len(lst) >= len(bomb):
		if lst[-len(bomb):] == bomb:
			for i in range(len(bomb)):
				lst.pop()
				
if lst:
	print(''.join(map(str,lst)))
	
else:
	print('EMPTY')
