# [BAEKJOON] 2635. 수 이어가기

num = int(input())
num_list = [num] # 입력받은 수 리스트에 넣고 시작
max_len = 0 # 최대 길이

for i in range(num+1):
  select = i # 선택 수
  num_list.append(i) # 리스트에 추가
  idx = 0 # 인덱스 0부터 시작
  while True:
    select = num_list[idx] - select # 다음 수 연산
    if select < 0: # 음수가 되면 반복문 종료
      break
    num_list.append(select) # 연산한 수 리스트에 추가
    idx += 1 # 인덱스 1씩 증가

  cnt = len(num_list) # 리스트 수 카운트
  if cnt > max_len: # 최대 길이 갱신
    max_len = cnt
    max_list = num_list[:] # 최대 길이 리스트 복사
  num_list = [num] # 리스트 초기화

print(max_len)
print(*max_list)