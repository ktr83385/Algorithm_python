import sys

string = list(sys.stdin.readline().strip().split())

count = 0

for _ in string:
    count += 1

print(count)