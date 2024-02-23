# [SWEA] 20281. 16진수 암호비트패턴 출력하기

hex_to_bin = {f'{i:X}' : f'{i:04b}' for i in range(16)}
encode_list = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']

T = int(input())

for test_case in range(1, T + 1):
  code = input().strip()
  bin_num = ''

  # 이진수 변환
  for i in code:
    bin_num += hex_to_bin[i]

  # 암호화
  cut = 0
  result = []
  for i in range(len(bin_num)):
    if bin_num[cut:cut+6] in encode_list:
      result.append(encode_list.index(bin_num[cut:cut+6]))
      cut += 6
    else:
      cut += 1

  print(f'#{test_case}', *result)