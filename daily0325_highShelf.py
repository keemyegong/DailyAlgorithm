# [SWEA] 1486. 장훈이의 높은 선반

def DFS(sum_height, cnt):
  global result
  # 백트래킹
  if sum_height >= result:
    return
  # 종료
  if sum_height >= top:
    result = sum_height
    return
  if cnt == N:
    return
  # 재귀 호출
  DFS(sum_height + heights[cnt], cnt+1) # 더하는 경우
  DFS(sum_height, cnt+1) # 더하지 않는 경우
 
for test_case in range(1, int(input())+1):
  N, top = map(int, input().split())
  heights = list(map(int, input().split()))
  result = 1e9
  DFS(0, 0) # sum_height, cnt
  
  print(f'#{test_case} {result-top}')