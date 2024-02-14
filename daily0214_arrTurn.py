
# [SWEA] 1961. 숫자 배열 회전

T = int(input())

for test_case in range(1, T+1):
  
  N = int(input())
  arr = [list(map(int, input().split())) for _ in range(N)]
  arr_90 = [[] for _ in range(N)]
  arr_180 = [[] for _ in range(N)]
  arr_270 = [[] for _ in range(N)]
  
  # 90도 회전
  for j in range(N):
    for i in range(N):
      arr_90[j].append(arr[N-i-1][j])
  
  # 180도 회전
  for i in range(N):
    for j in range(N):
      arr_180[i].append(arr[N-i-1][N-j-1])
  
  
  # 270도 회전
  for j in range(N):
    for i in range(N):
      arr_270[j].append(arr[i][N-j-1])
  
  print(f'#{test_case}')
  for i in range(N):
    print(''.join(map(str, arr_90[i])), ''.join(map(str, arr_180[i])), ''.join(map(str, arr_270[i])))