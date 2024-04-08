# [BAEKJOON] 2606. 바이러스 - BFS 풀이

from collections import deque

N = int(input()) # 컴퓨터의 수
line = int(input()) # 연결된 쌍의 수

graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

for i in range(line):
  node1, node2 = map(int, input().split())
  graph[node1][node2] = True
  graph[node2][node1] = True

def BFS(start): # 너비 우선 탐색
  global cnt
  q = deque([start]) # 시작점 넣고 출발
  visited[start] = True # 시작점 방문 처리
  
  while q: # 큐가 비어있을 떄까지 반복
    start = q.popleft()
    for i in range(2, N+1): # 라인 수만큼 탐색
      if not visited[i] and graph[start][i]:
        q.append(i)
        visited[i] = True
        cnt += 1

BFS(1)
print(cnt)