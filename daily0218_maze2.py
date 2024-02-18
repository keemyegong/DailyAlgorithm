# [SWEA] 1227. maze2
from collections import deque

dirs = [(0,-1), (0,1), (-1,0), (1,0)] # 이동 방향 상, 하, 좌, 우

for _ in range(1, 11):
  tc = int(input())
  maze = [list(map(int, input())) for _ in range(100)] # 100*100 미로

  q = deque([(1,1)]) # 시작 위치 설정
  maze[1][1] = 1 # 시작 위치 방문 기록

  result = 0 # 결과 기본값 0 설정

  # BFS 탐색 시작
  while q:
      cur_i, cur_j = q.popleft() # 현재 위치 pop

      if maze[cur_i][cur_j] == 3: # 도착점인 경우 결과 1 설정 후 반복문 종료
          result = 1
          break

      for d in dirs: # 상하좌우 이동
          ni, nj = cur_i + d[0], cur_j + d[1] # 이동값 설정
          if 0 <= ni < 100 and 0 <= nj < 100 and maze[ni][nj] != 1:
            # 배열을 벗어나지 않는 범위에서, 1이 아닐 때만
              maze[cur_i][cur_j] = 1 # 현재 위치 방문 기록
              q.append((ni, nj)) # 이동값 append

  print(f'#{tc} {result}')