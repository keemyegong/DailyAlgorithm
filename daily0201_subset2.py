'''
[SWEA] 19661 부분집합의 합 복습
10개의 원소 가진 집합 A가 있다.  집합 A의 부분 집합 중 공집합을 제외한 부분집합의 합이 0인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
예를 들어 {-1, 4, -3}의 부분집합은 모든 요소의 합이 0이므로 카운트를 세야한다.
'''


T = int(input())

for test_case in range(1, T + 1):
  
  cnt = 0
  arr = list(map(int, input().split()))
  
  for i in range(1 << 10):
    arr_list = []
    for j in range(10):
      if i & (1 << j):
        arr_list.append(arr[j])
    
    if sum(arr_list) == 0:
      cnt += 1
  
  print(f'#{test_case} {cnt-1}')