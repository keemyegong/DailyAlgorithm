# [SWEA] 1926. 간단한 369게임

N = int(input())

for i in range(1, N+1):
  cnt = 0 # 3, 6, 9 카운트 변수
  if '3' in str(i) or '6' in str(i) or '9' in str(i): # 3, 6, 9가 있을 경우
    for j in str(i):
      if j == '3' or j == '6' or j == '9':
        cnt += 1 # 3, 6, 9일 때마다 카운트 증가
    print('-'*cnt, end =' ') # 카운트만큼 - 출력
  else:
    print(i, end= ' ') # 아닐 경우 수 출력