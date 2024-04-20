# [BAEKJOON] 1181. 단어 정렬

import sys
input = sys.stdin.readline
N = int(input())
words = []

for _ in range(N):
  word = input().strip()
  if word not in words:
    words.append(word)

words.sort()
N = len(words)

def custom_sort(word):
  return len(word), word

words.sort(key=custom_sort)

for word in words:
  print(word)