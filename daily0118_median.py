#중앙값 구하기 함수
#인자로 배열이 주어질 때 중앙값 구하기
def solution(array):
    array.sort()
    answer = array[len(array)//2]
    return answer

print(solution([1, 3, 5, 4, 2]))