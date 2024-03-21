# [SWEA] 1238. Contact

# 문제 아이디어
# 가장 마지막에 연락을 받은 사람 = 해당 값에 도달하기까지 가장 오랜 시간이 걸리는 사람
# 즉, visited에 방문 횟수를 누적하면서 가장 큰 값을 찾으면 된다

from collections import deque

def contact(S):
  q = deque([(S)]) # 큐 생성

  while q: # 큐가 빌 때까지
    cur = q.popleft() # 현재 값 popleft

    for next in adjl[cur]: # 현재 값과 연결된 연락망 순회
      if visited[next]: # 중복 체크
        continue
      visited[next] = visited[cur] + 1 # 연락 횟수 +1씩 카운트
      q.append(next) # 해당 값 append

  return visited # 방문 기록 리스트 리턴 => 가장 큰 수의 인덱스를 찾기 위함

for test_case in range(1, 11):
  E, S = map(int, input().split()) # 연락 방향선 개수, 연락 리스트 길이
  lst = list(map(int, input().split())) # from, to 연락 방향 정보
  adjl = [[] for _ in range(max(lst)+1)] # 인접 리스트
  visited = [0] * (max(lst)+1) # 방문 기록 리스트

  for i in range(E//2):
    adjl[lst[i*2]].append(lst[i*2+1]) # 인접 리스트에 from, to 연락 정보 저장

  contact_cnt = contact(S) # 함수 호출을 통해 연락 횟수 저장 리스트 할당
  tmp = 0

  for i in range(len(contact_cnt)): # 연락 횟수 저장 리스트에서
    if contact_cnt[i] >= tmp: # 가장 큰 값의 마지막 인덱스 탐색
      tmp = contact_cnt[i]
      result = i
  
  print(f'#{test_case} {result}')