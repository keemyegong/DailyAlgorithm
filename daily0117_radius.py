#Quiz
#원의 넓이가 10 초과인 데이터만 출력하세요.
#map, filter 모두 사용

radius = [1,2,3,3,2.5,9]

#1.
filter_area = list(filter(lambda r: r ** 2 * 3.14 > 10, radius))
print(filter_area)
#radius 리스트 중 원의 넓이가 10을 초과하는 데이터만 출력

#2.
area = map(lambda r : r ** 2 * 3.14, radius)
filter_area = list(filter(lambda a: a > 10, area))
print(filter_area)
#area에 radius의 원의 넓이를 계산한 값들을 area에 넣고 개중 10을 초과하는 데이터만 출력

#3.
filter_area = list(filter(lambda a: a > 10, map(lambda x: x ** 2 * 3.14, radius)))
print(filter_area)
#radius의 원의 넓이를 계산한 값들 중 10을 초과하는 데이터만 출력