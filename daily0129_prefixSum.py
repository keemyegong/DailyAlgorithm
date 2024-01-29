#구간합 구하기
'''
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
'''

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split()) #정수 개수, 이웃한 M의 개수 변수에 할당
    cases = list(map(int, input().split())) #입력받은 N개의 정수를 리스트에 할당
    lst = []
    for i in range(N - M + 1): #이웃하는 배열 M을 제한 N만큼 반복
        total = 0
        total += sum(cases[i:i+M]) #i부터 배열 구간까지의 수 합산
        lst.append(total)
    result = max(lst) - min(lst) #결과값 계산
    print(f'#{test_case} {result}')