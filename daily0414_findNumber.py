# [BAEKJOON] 1316. 그룹 단어 체커

N = int(input()) # 단어 개수
cnt = 0

for _ in range(N):
  check = '' # 중복 단어 체크 문자열
  flag = True # 그룹 단어 판별
  word = input()
  for w in word:
    if w not in check: # 중복 단어가 아니라면 문자열에 추가
      check += w
    else: # 중복 단어라면
      if check[-1] != w: # 마지막 문자열과 일치하지 않을 때 F 판별
        flag = False
        break
  if flag: # 판별값이 True라면 카운트 증가
    cnt += 1

print(cnt)