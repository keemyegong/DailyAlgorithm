#문제 설명: 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2  #두 분모를 곱해 같은 수로 만들기
    numer = numer1 * denom2 + numer2 * denom1  #분자에도 각각의 분모를 곱해 통일

    n = min(numer, denom)  #통분을 위해 분모와 분자 중 더 작은 수를 변수 n에 할당
    answer = []
    
    while True:
        if denom % n == 0 and numer % n == 0:
            answer.append(int(numer/n))
            answer.append(int(denom/n))
            break  #분수와 분자 모두 n으로 나누어질 시 분자, 분모를 n으로 나누고 반복문 종료
        elif n == 1:
            break
        else:
            n -= 1  #나누어지지 않을 시 n을 1씩 차감하고 1이 되면 반복문 종료
    
    return answer

#풀이: 분모와 분자 중 더 작은 수를 n이라는 변수에 할당하고, n부터 -1씩 차감하며 공약수를 찾는다.