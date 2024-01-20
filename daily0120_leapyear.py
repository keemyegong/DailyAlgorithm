#윤년을 구하는 함수
#1. 기존 작성 코드
def leapYear(year):
  if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    return True
  elif year % 4 == 0 and year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True

print(leapYear(int(input())))

#2. 기존 코드 간소화
def leapYear2(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False

print(leapYear2(int(input())))