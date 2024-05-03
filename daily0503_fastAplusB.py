# [BAEKJOON] 15552. 빠른 A + B
import sys
input = sys.stdin.readline

for test_case in range(int(input())):
    A, B = map(int, input().split())
    print(A + B)