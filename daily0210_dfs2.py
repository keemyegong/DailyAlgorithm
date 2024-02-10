'''
[SWEA] 4871. 그래프 경로
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
'''

T = int(input())

for test_case in range(1, T + 1):
  V, E = map(int, input().split()) # V: 노드 개수, E: 간선 개수
  
  adj_list = [[] for _ in range(V+1)]

  for i in range(E):
    n1, n2 = map(int, input().split())
    adj_list[n1].append(n2) # 인접 정보 리스트
    
  S, G = map(int, input().split()) # S: 출발점, G: 도착점
  
  visit = [0] * (V+1) # 방문 기록 리스트
  stack = [S] # 출발점부터 DFS 시작
  
  while stack: # 스택 안에 남은 것이 없을 때까지
    node = stack.pop() # 현재 방문할 노드 pop
    
    if visit[node] == False: # 해당 노드에 방문한 적이 없다면
      visit[node] = 1 # 방문 처리
      
      for next_node in adj_list[node]: # 연결된 노드 순회
        if visit[next_node] == False: # 이웃 노드에 방문하지 않았다면
          stack.append(next_node) # 스택에 추가
  
  if visit[G]:
    result = 1 # 도착점 노드에 방문 기록이 있다면 1
  else:
    result = 0 # 방문 기록이 없다면 0
  
  print(f'#{test_case} {result}')