# [SWEA] 5188. 최소 합

def find_min(i, j, s): # 좌표 i, j, 합계
  global min_s # 전역 변수 설정

  if i == N-1 and j == N-1: # 끝 지점에 도달하면
    if min_s > s: # 최소 합 갱신
      min_s = s
    return
  elif s >= min_s: # 가지치기
    return
  else:
    for d in dirs: # 방향 순회
      ni, nj = i + d[0], j + d[1] # 새로운 위치 계산
      if 0 <= ni < N and 0 <= nj < N: # 배열을 벗어나지 않는 범위에서
        find_min(ni, nj, s + arr[ni][nj])
          # 재귀 호출을 통해 새로운 위치 이동
          # 다음 위치의 값을 합산하며 합계 업데이트

T = int(input())

dirs = [(0,1),(1,0)] # 오른쪽, 아래 방향 설정

for tc in range(1, T+1):
  N = int(input()) # 배열 크기
  arr = [list(map(int, input().split())) for _ in range(N)] # 배열
  min_s = 13*2*10 # 최소 합계

  find_min(0, 0, arr[0][0]) # (0,0)부터 시작값 넣고 호출

  print(f'#{tc} {min_s}')