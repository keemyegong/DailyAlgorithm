# [SWEA] 1952. 수영장
# DFS 재귀함수 백트래킹

def DFS(cur_sum, month):
  global result
  # 가지치기
  if cur_sum >= result:
    return
  # 종료 조건
  if month > 12:
    result = cur_sum
    return
  # 재귀 호출
  DFS(cur_sum + cost[0] * plan[month], month + 1) # 1일권
  DFS(cur_sum + cost[1], month + 1) # 1개월권
  DFS(cur_sum + cost[2], month + 3) # 3개월권
  DFS(cur_sum + cost[3], month + 12) # 연간권

for test_case in range(1, int(input())+1):
  cost = list(map(int, input().split()))
  plan = [0] + list(map(int, input().split()))
  result = 10e9 # 최소값 갱신 결과 초기화
  
  DFS(0, 1) # 합계, 월
  
  print(f'#{test_case} {result}')