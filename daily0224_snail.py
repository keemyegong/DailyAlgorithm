# [SWEA] 1954. 달팽이 숫자

T = int(input())

dirs = [(0,1), (1,0), (0,-1), (-1,0)] # 우, 하, 좌, 상

for test_case in range(1, T+1):
  N = int(input())
  nums = list(range(1, N**2+1)) # 숫자 리스트
  arr = [[0] * N for _ in range(N)] # 숫자를 채울 배열

  num_idx = 0  # nums 리스트의 인덱스
  cur_x, cur_y = 0, 0  # 현재 위치
  d = 0  # 현재 이동 방향

  while num_idx < N**2:  # 모든 칸에 숫자를 채울 때까지 반복
    arr[cur_x][cur_y] = nums[num_idx]  # 현재 위치에 숫자를 채움
    num_idx += 1  # 다음 숫자로 이동
    nx, ny = cur_x + dirs[d][0], cur_y + dirs[d][1]  # 다음 위치 계산
    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:  # 다음 위치가 배열 범위 내이고 아직 숫자가 채워지지 않았다면
      cur_x, cur_y = nx, ny  # 다음 위치로 이동
    else:  # 다음 위치가 배열 범위를 벗어나거나 이미 숫자가 채워져 있다면
      d = (d + 1) % 4  # 이동 방향을 변경 (시계방향으로 변경)
      cur_x, cur_y = cur_x + dirs[d][0], cur_y + dirs[d][1]  # 다음 위치로 이동
      
    print(f'#{test_case}')
    for row in arr:
      print(*row)
