# [SWEA] 5208. 전기버스2

def find_min(cur, cnt):
  global min_cnt
  if min_cnt <= cnt: # 가지치기
    return
  if cur + charge[cur] >= N-1:
    if min_cnt > cnt:
      min_cnt = cnt
    return
  else: # 탐색 수행
    for i in range(cur + 1, cur + charge[cur] + 1):
      find_min(i, cnt + 1)

for test_case in range(1, int(input())+1):
  N, *charge = map(int, input().split())
  # N: 정류장 수, charge: 충전지
  min_cnt = N
  find_min(0, 0) # 현재 위치, 충전 횟수

  print(f'#{test_case} {min_cnt}')