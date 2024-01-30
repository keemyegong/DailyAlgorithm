'''
[SWEA] 4834 숫자 카드

0에서 9까지 숫자가 적힌 N장의 카드가 주어진다. 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
'''

T = int(input())

for test_case in range(1, T + 1):
  N = int(input())
  card = input()
  
  cards = list(map(int, card)) #cards 리스트 생성
  cnt_list = [0] * (max(cards) + 1) #카드의 개수를 카운트하는 cnt_list 생성
  
  for c in cards:
    cnt_list[c] += 1 #카드 수 카운트
  
  max_c = max(cnt_list) #개수가 가장 많은 카드 max_c에 할당
  max_idx = 0
  
  for i in range(len(cnt_list)):
    if cnt_list[i] == max_c:
      max_idx = i #max_c의 인덱스 구하기, 적힌 숫자가 큰 쪽이 할당됨
  
  print(f'#{test_case} {max_idx} {max_c}')