def solution(array):
  num_list = [0] * (max(array) + 1)
  
  for i in array:
    num_list[i] += 1
  
  count = 0
  for n in num_list:
    if n == max(num_list):
      count += 1
  
  if count > 1:
    return -1
  else:
    return num_list.index(max(num_list))