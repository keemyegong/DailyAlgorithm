'''
[SWEA] 1974. 스도쿠 검증
과정
1. 행 중복 검사
2. 열 중복 검사
3. 3*3 칸 검사
4. fail 변수를 통해 검증
'''

T = int(input())

for test_case in range(1, T+1):
  arr = [list(map(int, input().split())) for _ in range(9)]
  fail = 0
  
  # 행 중복 검사
  for i in range(9):
    row_list = []
    for j in range(9):
      if arr[i][j] not in row_list:
        row_list.append(arr[i][j])
      else:
        fail += 1
  
  # 열 중복 검사
  for j in range(9):
    col_list = []
    for i in range(9):
      if arr[i][j] not in col_list:
        col_list.append(arr[i][j])
      else:
        fail += 1
  
  # 3*3 중복 검사
  
  for i in range(0, 9, 3):
    for j in range(0, 9, 3):
      square_list = []
      check_list = []
      for k in range(3):
        square_list.append(arr[i][j+k])
        square_list.append(arr[i+1][j+k])
        square_list.append(arr[i+2][j+k])
    for v in square_list:
      if v not in check_list:
        check_list.append(v)
      else:
        fail += 1
      
  if fail > 0:
    result = 0
  else:
    result = 1
    
  print(f'#{test_case} {result}')
  
# 느낀 점
# 코드를 더 효율적으로 구현하는 방법이 분명히 있을 텐데 머리가 돌아가지 않는다 추후 보강하면 좋을 것 같다