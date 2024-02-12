T = int(input())
 
for test_case in range(1, T + 1):
  N, M = map(int, input().split())
  arr = [list(map(int, input().split())) for _ in range(N)]
   
  def dirs(M): # 주어지는 m에 따라 방향 만들기
    result_list = []
    for i in range(M):
      for j in range(M):
        result_list.extend([(i, j)])
    return result_list
   
  max_sum = 0 # 최대 합 할당 및 초기화 역할
  for i in range(N):
    for j in range(N):
      sum_result = 0
      for d in dirs(M): # m에 따라 만든 델타 리스트에서 반복 시작
        ni = i + d[0]
        nj = j + d[1]
        if 0 <= ni < N and 0 <= nj < N: # 배열을 벗어나지 않는 한에서
          sum_result += arr[ni][nj] # 값 합산
           
      if sum_result > max_sum: # 최대 합 비교
        max_sum = sum_result
           
  print(f'#{test_case} {max_sum}')
