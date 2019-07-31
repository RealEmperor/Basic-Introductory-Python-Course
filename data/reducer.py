# mapper.py
import sys

word_dict = {}
for line in sys.stdin:
    ls = line.split(',')
    word_dict.setdefault(ls[0], 0)
    word_dict[ls[0]] += int(ls[1])

for word in word_dict:
    print(word, word_dict[word])
