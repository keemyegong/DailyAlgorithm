'''
[SWEA] 1219. 길 찾기
'''

T = 10

for test_case in range(1, T + 1):
  tc, E = map(int, input().split()) # tc: 테스트케이스, E: 노드 개수
  arr = list(map(int, input().split())) # 순서쌍
  
  adj_list = [[] for _ in range(100)]
  
  for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    adj_list[n1].append(n2) # 인접 정보 리스트
    
  visit = [0] * 100 # 방문 기록 리스트
  stack = [0] 

  while stack: # 스택 안에 남은 것이 없을 때까지
    node = stack.pop() # 방문할 스택 pop
    
    if visit[node] == False:
      visit[node] = 1 # 방문하지 않았다면 방문 기록

      for next_node in adj_list[node]:
          if not visit[next_node]:
              stack.append(next_node) # 연결된 노드들 중 방문하지 않은 노드stack에 추가
  
  if visit[99]:
    result = 1 # 99번 노드(도착점)에 방문 기록이 있다면 1
  else:
    result = 0 # 방문 기록이 없다면 0
    
  print(f'#{test_case} {result}')