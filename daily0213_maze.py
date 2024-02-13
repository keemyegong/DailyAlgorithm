'''
[SWEA] 4875. 미로
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다. 주어진 미로 밖으로는 나갈 수 없다.
'''

T = int(input())

dirs = [(0,-1), (0,1), (-1,0), (1,0)]

for test_case in range(1, T+1):
  N = int(input())
  arr = [list(map(int, input().strip())) for _ in range(N)]
  stack = []

  # start index 찾기
  for i in range(N):
    if 2 in arr[i]:
      si, sj = i, arr[i].index(2)
      break

  # 미로 찾기
  stack.append((si, sj)) # 출발지 설정

  result = 0 # 기본값 0
  
  while stack:
    cur_i, cur_j = stack.pop()
    
    if arr[cur_i][cur_j] == 1:
      continue
    
    if arr[cur_i][cur_j] == 3:
      result = 1
      break
    
    arr[cur_i][cur_j] = 1
    
    for d in dirs:
      ni = cur_i + d[0]
      nj = cur_j + d[1]

      if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1:
        stack.append((ni, nj))
  
  print(f'#{test_case} {result}')
