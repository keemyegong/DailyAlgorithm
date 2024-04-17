# [BAEKJOON] 2839. 설탕 배달

kg = int(input()) # 설탕 kg
cnt = 0 # 봉지 수

while kg >= 0: # kg가 0 이상일 동안
  if kg % 5 == 0: # kg가 5로 나누어 떨어지면 종료 (kg가 0인 케이스 포함)
    cnt += kg // 5
    break
  else: # 5로 나누어 떨어지지 않으면 3씩 차감하면서 반복
    kg -= 3
    cnt += 1
else: # 나누어 떨어지지 않아 break 문에 걸리지 않을 경우
  cnt = -1        
            
print(cnt)