# [SWEA] 4012. 요리사

def DFS(cur, cnt):
  global result
  # 종료 조건
  if cnt == N//2:
    sum_a, sum_b = 0, 0
    for i in range(N-1):
      for j in range(i+1, N):
        if visited[i] and visited[j]:
          sum_a += arr[i][j] + arr[j][i]
        elif not visited[i] and not visited[j]:
          sum_b += arr[i][j] + arr[j][i]
    result = min(result, abs(sum_a - sum_b))
  for next in range(cur, N):
    if visited[next]:
      continue
    visited[next] = 1
    DFS(next + 1, cnt + 1)
    visited[next] = 0

for test_case in range(1, int(input())+1):
  N = int(input()) # 식재료의 수
  arr = [list(map(int, input().split())) for _ in range(N)]
  
  visited = [0] * (N+1)
  result = 10e9

  DFS(0, 0) # 현재 위치, 재료 개수

  print(f'#{test_case} {result}')