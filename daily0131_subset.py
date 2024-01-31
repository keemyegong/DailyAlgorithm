'''
[SWEA] 4837 부분집합의 합

1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.
'''

T = int(input())
arr = list(range(1, 13))
 
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    # N = 찾을 부분집합 내 원소의 개수
    # K = 찾을 부분집합 내 원소의 합
 
    cnt = 0
 
    for i in range(1 << 12):
        arr_list = []
        for j in range(12):
            if i & (1 << j):
                arr_list.append(arr[j])
                #부분집합 리스트 만들기 끝
        if sum(arr_list) == K and len(arr_list) == N:
            cnt += 1
            #조건 판별
 
    print(f'#{test_case} {cnt}')