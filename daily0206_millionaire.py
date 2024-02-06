'''
[SWEA] 1859. 백만장자 프로젝트

- 문제 해석
입력: 일수 N(int), N일 동안의 매매가(list)
출력: N일 동안 N개의 매매가에서 얻을 수 있는 최대 이익
- 요구 조건
1) 하루에 1만큼만 구입 가능
2) 판매는 얼마든지 가능
3) 매매가는 10,000 이하
- 참고
1) 첫째 날에는 판매 X
2) 마지막 날에는 구매 X
3) 구매하지 않는 게 최대 이익일 수도 있음
'''

T = int(input())

for test_case in range(1, T + 1):
  N = int(input())
  price = list(map(int, input().split()))
  
  profit = 0
  max_price = price[-1]
  
  for i in range(N-2, -1, -1): # 마지막 값은 비교에 필요 없으므로 N-2부터 시작
    if price[i] > max_price:
      max_price = price[i]
    elif price[i] < max_price:
      profit += max_price - price[i]
            
  print(f'#{test_case} {profit}')