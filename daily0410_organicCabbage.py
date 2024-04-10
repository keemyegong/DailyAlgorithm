# [BAEKJOON] 1012. 유기농 배추

from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1 ,0)] # 상하좌우 이동 방향

def BFS(i, j): # 너비 우선 탐색
  global cnt
  q = deque([(i, j)]) # 출발점 넣고 시작
  arr[i][j] = 0 # 방문한 곳 0 처리
  while q: # 큐가 비어있을 때까지
    cur_i, cur_j = q.popleft() # 방문할 위치 popleft
    for d in dirs: # 상/하/좌/우 이동
      ni, nj = cur_i + d[0], cur_j + d[1]
      if 0 <= ni < N and 0 <= nj < M and arr[ni][nj]: # 배열 범위 내에서 값이 1일 때
        q.append((ni, nj)) # 이동 위치 append
        arr[ni][nj] = 0 # 방문한 곳 0 처리
  cnt += 1 # 탐색이 끝나면 카운트 +1

for test_case in range(int(input())):
  M, N, K = map(int, input().split())  
  arr = [[0] * M for _ in range(N)]
  cnt = 0
  
  for _ in range(K): 
    x, y = map(int, input().split())
    arr[y][x] = 1

  for i in range(N): # 1일 때 너비우선탐색
    for j in range(M):
      if arr[i][j] == 1:
        BFS(i, j)
  
  print(cnt)