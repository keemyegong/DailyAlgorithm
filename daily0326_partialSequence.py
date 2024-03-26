
# [SWEA] 2817. 부분 수열의 합

def DFS(cur_sum, cnt, start):
  global result
  if cur_sum > target: # 현재 합이 타겟 값보다 크면
    return
  # 종료 조건
  if cur_sum == target: # 현재 합이 타겟 값과 같은 경우
    result += 1
    return
  if cnt == N:
    return
  # 재귀 호출
  for i in range(start, N):
    if visited[i]:
      continue
    visited[i] = 1
    DFS(cur_sum + nums[i], cnt+1, i+1)
    visited[i] = 0

for test_case in range(1, int(input())+1):
  N, target = map(int, input().split())
  # N: 수열의 길이, target: 타겟 합계
  nums = list(map(int, input().split()))
  visited = [0] * N
  result = 0

  DFS(0, 0, 0) # 합계, 카운트, 시작 인덱스

  print(f'#{test_case} {result}')