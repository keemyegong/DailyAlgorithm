# [BAEKJOON] 2667. 단지번호붙이기

from collections import deque

N = int(input())
map = [list(map(int, input())) for _ in range(N)]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 상하좌우 이동값

def BFS(i, j): # 너비우선탐색
  q = deque([(i, j)]) # 출발점 넣고 시작
  map[i][j] = 0 # 방문 표시
  cnt = 1
  while q: # 큐가 비어있을 때까지
    cur_i, cur_j = q.popleft() # 현재 위치 popleft
    for d in dirs: # 방향 이동
      ni, nj = cur_i + d[0], cur_j + d[1] # 이동 위치 설정
      if 0 <= ni < N and 0 <= nj < N and map[ni][nj] == 1:
        map[ni][nj] = 0 # 방문 표시
        q.append((ni, nj)) # 이동 위치 append
        cnt += 1 # 개수 카운트
  return cnt

cnt_list = [] # 빌리지 개수 리스트
for i in range(N): # 리스트 순회하며 빌리지 탐색
  for j in range(N):
    if map[i][j] == 1: # 값이 1일 때 BFS
      cnt = BFS(i, j)
      cnt_list.append(cnt)

cnt_list.sort() # 리스트 오름차순 정렬
print(len(cnt_list))
for cnt in cnt_list:
  print(cnt)