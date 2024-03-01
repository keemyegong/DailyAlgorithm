# [BAEKJOON] 13300. 방 배정

n, m = map(int, input().split()) # n: 총 인원, m: 각 방 최대 인원
rooms = [[0, 0] for _ in range(6)] # 방 리스트

# 방에 성별, 학년 할당
for i in range(n):
  gender, grade = map(int, input().split())
  grade -= 1
  if gender == 0:
    rooms[grade][0] += 1
  elif gender == 1:
    rooms[grade][1] += 1
    
result = 0

# 방 개수 구하기
for i in range(6):
  if 0 < rooms[i][0] < m:
    result += 1
  else:
    result += rooms[i][0] // m
    if rooms[i][0] % m > 0:
      result += 1
  if 0 < rooms[i][1] < m:
    result += 1
  else:
    result += rooms[i][1] // m
    if rooms[i][1] % m > 0:
      result += 1

print(result)

'''
1. 문제 해석
입력
- n: 수학여행 참가 인원, m: 한 방의 최대 인원 수
- gender: 성별, grade: 학년 * N
출력
- 최소한의 방 수
요구 사항
- 남학생, 여학생 방 따로
- 학년별 방 따로
=> 같은 학년, 같은 성별끼리만 같은 방 사용 가능
- 각 방의 최대 인원 정해져 있음
2. 구조 설계
아이디어
- [[0,0]*6] 학년별 리스트 생성
- 내부 리스트의 0번 인덱스에 여, 1번 인덱스에 남
- 마지막에 반복문으로 각 인덱스를 m으로 나눠 최소 방 수 출력
필요 변수
- rooms: 학년별 방 리스트
'''