#백준 2588번
#세 자리 수 곱셈의 과정 값 출력

a = input()
b = input()

n1 = int(a) * int(b[2])
n2 = int(a) * int(b[1])
n3 = int(a) * int(b[0])
n4 = int(a) * int(b)

print(n1)
print(n2)
print(n3)
print(n4)