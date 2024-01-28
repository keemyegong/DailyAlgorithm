def str_strip(text, remove_ch):
  cut1 = 0
  cut2 = 0
  for i in range(len(text)):
    if text[i] != remove_ch:
      cut1 = i
      break
  for i in range(len(text)):
    if text[-i] != remove_ch:
      cut2 = -i
      break
  return text[cut1:cut2+1]

print(str_strip('---i-want-to-eat-don--ut---', '-'))