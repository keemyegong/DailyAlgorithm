# [SWEA] 5174. subtree

def subtree(node):
    global cnt
    if node != 0:
        cnt += 1
        subtree(left[node])
        subtree(right[node])
    return cnt
 
T = int(input())
 
for test_case in range(1, T+1):
    E, N = map(int, input().split()) # E: 간선 개수, N: 탐색 시작 노드
    tree = list(map(int, input().split()))
    cnt = 0 # 개수 세기
    left = [0] * (E + 2) 
    right = [0] * (E + 2)
 
    for i in range(E):
        p, c = tree[i*2], tree[i*2 + 1]
        if left[p] == 0: # 왼쪽 노드 저장
            left[p] = c
        else:  # 오른쪽 노드 저장
            right[p] = c
 
    print(f'#{test_case}', subtree(N))
