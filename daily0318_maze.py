# [BAEKJOON] 2178. 미로 탐색

from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # i, j 이동 방향

N, M = map(int, input().split()) # N: 미로 세로 길이, M: 미로 가로 길이
maze = [list(map(int, input().strip())) for _ in range(N)] # N*M 미로
visited = [[False] * M for _ in range(N)] # 방문 기록 리스트

q = deque([(0, 0)]) # 시작 인덱스 큐에 넣고 시작
visited[0][0] = True # 시작 인덱스 방문 처리

while q: # 큐가 비어 있을 때까지
  cur_i, cur_j = q.popleft() # 현재 위치 popleft => 너비우선탐색
  
  if cur_i == N-1 and cur_j == M-1: # 도착점에 도달하면
    print(visited[cur_i][cur_j]) # 이동 횟수 출력
    break
  
  for d in dirs: # 상하좌우 이동
    ni, nj = cur_i + d[0], cur_j + d[1]
    if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == 1 and not visited[ni][nj]:
      # 배열의 범위를 벗어나지 않는 내에서, 방문한 적 없는 1이면
      visited[ni][nj] = visited[cur_i][cur_j] + 1 # 이동 횟수를 누적하며 방문 기록
      q.append((ni, nj)) # 이동 위치 append