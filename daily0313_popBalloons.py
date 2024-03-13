# [BAEKJOON] 2346. 풍선 터뜨리기

from collections import deque

n = int(input())
# 풍선 개수
balloons = deque(map(int, input().split()))
# 풍선 리스트
balloons = deque((index+1, value) for index, value in enumerate(balloons))
# 풍선 리스트에 각 풍선의 인덱스 함께 저장
result = []
# 터지는 풍선의 인덱스를 담을 결과 리스트

while balloons: # 풍선이 남아있는 동안
  pang = balloons.popleft() # 풍선 터뜨리기
  num = pang[1] # 풍선 value
  result.append(pang[0]) # 풍선 idx
  
  if num > 0: # value가 양수일 때
    for i in range(num-1): # value만큼
      if balloons: # 풍선이 남아있는 동안에만
        tmp = balloons.popleft()
        balloons.append(tmp)
        # 왼쪽에서 pop, 오른쪽에 append 하며 우측으로 순회
  else: # value가 음수일 때
    for i in range(abs(num)):
      if balloons:
        tmp = balloons.pop()
        balloons.appendleft(tmp)
        # 오른쪽에서 pop, 왼쪽에 append 하며 좌측으로 순회

print(*result)