T = int(input())

for test_case in range(1, T+1):
    N = int(input()) # 노선 개수
    arr = [0]*5001

    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            arr[j] += 1

    P = int(input())

    busstop = [int(input()) for _ in range(P)]

    print(f'#{test_case}', ' '.join(str(arr[i]) for i in busstop))