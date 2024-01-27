# split 함수 구현
# 1. sep 문자 한 개를 구분자로 text를 잘라서 리스트로 반환
def str_split(text, sep=' ') :
    str_list = []
    cut = 0
    for i in range(len(text)):
        if text[i] == sep:
            str_list.append(text[cut:i])
            cut = i + 1
    str_list.append(text[cut:])
    return str_list

print(str_split('i am too tired now',  ' '))

#2. sep 문자열을 구분자로 text를 잘라서 리스트로 반환
def str_split(text, sep='  ') : 
    str_list = []
    cut = 0
    for i in range(len(text)):
        if text[i:len(sep) + i] == sep:
            str_list.append(text[cut:i])
            cut = i + len(sep)
    str_list.append(text[cut:])
    return str_list

print(str_split('i am too tired  now',  '  '))
