# [SWEA] 12712. 파리 퇴치 3
T = int(input())

dirs1 = [(0,1), (1,0), (0,-1), (-1,0)] # 상하좌우
dirs2 = [(1,1), (-1,-1), (1,-1), (-1,1)] # 대각선

for test_case in range(1, T+1):
  N, M = map(int, input().split())
  arr = [list(map(int, input().split())) for _ in range(N)]
  
  max_sum = 0
  
  for i in range(N):
    for j in range(N):
      cur_sum1 = arr[i][j]
      cur_sum2 = arr[i][j]
      for d in dirs1:
        for k in range(1, M):
          ni = d[0] * k + i
          nj = d[1] * k + j
          if 0 <= ni < N and 0 <= nj < N:
            cur_sum1 += arr[ni][nj]
      for d in dirs2:
        for k in range(1, M):
          ni = d[0] * k + i
          nj = d[1] * k + j
          if 0 <= ni < N and 0 <= nj < N:
            cur_sum2 += arr[ni][nj]
      max_sum = max(max_sum, cur_sum1, cur_sum2)
  
  print(f'#{test_case} {max_sum}')