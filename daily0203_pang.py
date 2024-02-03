'''
[SWEA] 16268 풍선팡2
종이 꽃가루가 들어있는 풍선이 NxM 크기의 격자판에 붙어있는데, 어떤 풍선을 터뜨리면 상하좌우의 풍선이 추가로 터진다고 한다. 다음의 경우 가운데 풍선을 터뜨리면 상하좌우의 풍선이 추가로 1개씩 터지면서 총 5개의 꽃가루가 날리게 된다.
NxM개의 풍선에 들어있는 종이 꽃가루 개수A가 주어지면, 한 개의 풍선을 선택해 터뜨렸을 때 날릴 수 있는 꽃가루 수 중 최대값을 출력하는 프로그램을 만드시오.
'''

T = int(input())
dirs = [(0,0), (0,1), (0,-1), (1,0), (-1,0)]

for test_case in range(1, T + 1):
  N, M = map(int, input().split())
  arr = [list(map(int, input().split())) for _ in range(N)]
  
  result_list = []
  
  for i in range(N):
    for j in range(M):
      sum_result = 0
      for d in dirs:
        ni = i + d[0]
        nj = j + d[1]
        
        if 0 <= ni < N and 0 <= nj < M:
          sum_result += arr[ni][nj]
      result_list.append(sum_result)
          
  print(f'#{test_case} {max(sum_result)}')