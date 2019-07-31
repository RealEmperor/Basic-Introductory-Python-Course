# mapper.py
import sys

for line in sys.stdin:
    ls = line.split()
    for word in ls:
        if len(word.strip()) != 0:
            print(word + ',' + str(1))
