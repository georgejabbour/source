# Uses python3
# There are two ways of running this program:
# 1. Run
#     python3 APlusB.py
# then enter two numbers and press ctrl-d/ctrl-z
# 2. Save two numbers to a file -- say, dataset.txt.
# Then run
#     python3 APlusB.py < dataset.txt

import sys

# r = input()
# tokens = r.split()
# print(int(tokens[0]) + int(tokens[1]))

r = sys.stdin.readline()
tokens = r.split()
print(int(tokens[0]) + int(tokens[1]))