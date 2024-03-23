# [SWEA] 1865. 동철이의 일 분배

def DFS(idx, cur_sum):
  global result
  # 백트래킹
  if result >= cur_sum:
    return
  # 종료 조건
  if idx == N:
    result = cur_sum
    return
  # 재귀 호출
  for i in range(N):
    if not visited[i]:
      visited[i] = 1
      DFS(idx+1, cur_sum * (arr[idx][i]/100))
      visited[i] = 0

for test_case in range(1, int(input())+1):
  N = int(input())
  arr = [list(map(int, input().split())) for _ in range(N)]
  visited = [0] * N
  result = 0

  DFS(0, 1) # idx

  print(f'#{test_case} {result*100:.6f}')