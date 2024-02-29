# [BAEKJOON] 1244. 스위치 켜고 끄기

N = int(input())  # 스위치 개수
switch = list(map(int, input().split()))  # 스위치 배열
student = int(input())  # 학생 수

for _ in range(student):
  gender, num = map(int, input().split())  # 성별, 자연수

  if gender == 1:  # 남학생이면
    # 받은 스위치 넘버의 배수에 해당하는 스위치 상태를 반전
    for j in range(1, N+1):
      if j % num == 0:
        switch[j-1] = 1 - switch[j-1]

  elif gender == 2:  # 여학생이면
    num -= 1  # 인덱스를 이용하기 위해 -1
    # 받은 스위치를 누르고 주위 대칭적인 스위치를 확인하여 대칭이라면 상태 반전
    switch[num] = 1 - switch[num]
    for j in range(1, N-num+2):
      if num-j >= 0 and num+j < N:
        if switch[num-j] == switch[num+j]:  # 대칭인 스위치라면
          switch[num-j] = 1 - switch[num-j] 
          switch[num+j] = 1 - switch[num+j]  
        else:
          break  

# 20개씩 스위치 상태를 출력
for i in range(0, N, 20):
  print(*switch[i:i+20])