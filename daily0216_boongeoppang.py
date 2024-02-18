# [SWEA] 1860. 진기의 최고급 붕어빵

T = int(input())

for test_case in range(1, T + 1):
  n, m, k = map(int, input().split())
  # n: 사람 수
  # m: 붕어빵 제조 시간
  # k: 제조 개수
  visits = list(map(int, input().split())) # 방문자 시간 리스트
  visits.sort() # 먼저 온 사람 순서대로
  visited = [] # 방문한 사람 기록 리스트

  made = 0 # 붕어빵 개수
  rest = 0 # 남은 시간
  
  result = 'Impossible'

  while True:
    visit = visits.pop(0) # 방문자 꺼내기
      
    if visit == 0: # 0이면 장사 종료
      break

    made = (visit // m) * k - len(visited) - 1 # 붕어빵 제조 

    if made < 0: # 붕어빵 부족하면 장사 종료
        break

    visited.append(visit) # 방문한 사람 기록
    
    if len(visited) == n: # 모든 사람이 방문에 성공했으면
      result = 'Possible'
      break

  print(f'#{test_case} {result}')
