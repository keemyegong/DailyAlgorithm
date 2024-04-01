# [SWEA] 1220. Magnetic

T = 10

for test_case in range(1, T + 1):
  N = int(input())
  arr = [list(map(int, input().split())) for _ in range(N)]

  cnt = 0
  for j in range(N):
    pre = 0
    for i in range(N):
      if arr[i][j] == 1:
        pre = 1
      elif arr[i][j] == 2 and pre == 1:
        cnt += 1
        pre = 2

  print(f'#{test_case} {cnt}')
